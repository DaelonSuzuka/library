#!/usr/bin/env python3
"""Parse Microchip XC8 device header (.h) files into structured JSON.

Extracts register definitions including:
- Register name and address
- Bit field names, positions, sizes, and masks
- SFR type (8-bit, 16-bit, etc.)

Output: JSON array of register objects, one per register.

Usage:
  uv run python parse_header.py pic18f16q41.h -o pic18f16q41_registers.json
  uv run python parse_header.py pic18f16q41.h  # stdout
"""

import re
import json
import sys
import argparse
from pathlib import Path


def parse_header(filepath: str) -> list[dict]:
    """Parse a Microchip XC8 header file into a list of register dicts."""
    text = Path(filepath).read_text()
    lines = text.split('\n')

    registers = []
    current_reg = None

    # Patterns
    reg_comment = re.compile(r'^//\s*Register:\s+(\S+)')
    sfr_decl = re.compile(r'extern\s+volatile\s+(?:unsigned\s+)?(\w+)\s+(\w+)\s+__at\((0x[0-9A-Fa-f]+)\)')
    field_macro = re.compile(r'^#define\s+_(\w+)_POSN\s+(0x[0-9A-Fa-f]+|\d+)')
    field_size = re.compile(r'^#define\s+_(\w+)_SIZE\s+(0x[0-9A-Fa-f]+|\d+)')
    field_mask = re.compile(r'^#define\s+_(\w+)_MASK\s+(0x[0-9A-Fa-f]+|\d+)')

    for line in lines:
        # Register comment
        m = reg_comment.match(line)
        if m:
            current_reg = {
                'name': m.group(1),
                'address': None,
                'width': None,
                'fields': {},
            }
            registers.append(current_reg)
            continue

        # SFR declaration: type, name, address
        m = sfr_decl.search(line)
        if m and current_reg:
            type_str = m.group(1)
            name = m.group(2)
            addr = m.group(3)
            # Only update if this declaration matches the current register
            # (headers have both short and prefixed names)
            if name == current_reg['name'] or name == current_reg['name'] + 'bits':
                if name == current_reg['name']:
                    current_reg['address'] = int(addr, 16)
                    # Infer width from type
                    if 'char' in type_str or type_str == 'uint8_t':
                        current_reg['width'] = 8
                    elif 'int' in type_str and 'short' not in type_str:
                        current_reg['width'] = 16
                    elif 'long' in type_str:
                        current_reg['width'] = 32

        # Field macros: _REGFIELD_POSN, _SIZE, _MASK
        m = field_macro.match(line)
        if m and current_reg:
            # Only keep the "primary" field macros (not the prefixed copies)
            # Primary fields don't have the register name as prefix in the field name
            field_name = m.group(1)
            posn = int(m.group(2), 16) if m.group(2).startswith('0x') else int(m.group(2))
            current_reg['fields'][field_name] = current_reg['fields'].get(field_name, {})
            current_reg['fields'][field_name]['posn'] = posn

        m = field_size.match(line)
        if m and current_reg:
            field_name = m.group(1)
            size = int(m.group(2), 16) if m.group(2).startswith('0x') else int(m.group(2))
            current_reg['fields'][field_name] = current_reg['fields'].get(field_name, {})
            current_reg['fields'][field_name]['size'] = size

        m = field_mask.match(line)
        if m and current_reg:
            field_name = m.group(1)
            mask = int(m.group(2), 16) if m.group(2).startswith('0x') else int(m.group(2))
            current_reg['fields'][field_name] = current_reg['fields'].get(field_name, {})
            current_reg['fields'][field_name]['mask'] = mask

    # Post-process: separate primary fields from aliased (prefixed) fields
    # Primary fields: simple name like OUTPS, MD16, EN
    # Aliased fields: prefixed like T0OUTPS, T0MD16, T0EN
    # We keep both but mark the distinction
    for reg in registers:
        if not reg['fields']:
            continue
        primary_fields = {}
        alias_fields = {}
        reg_prefix = reg['name'].rstrip('0123456789') if reg['name'] else ''

        for fname, fdata in reg['fields'].items():
            # A field is primary if removing the register prefix doesn't change it
            # or if it's a single-bit field (bit0, bit1, etc.)
            if fname.startswith(reg_prefix) and len(fname) > len(reg_prefix):
                # This might be an alias — check if the unprefixed version also exists
                short = fname[len(reg_prefix):]
                # Only treat as alias if the short name exists as a field
                # and the short name was defined at the same position
                if short in reg['fields'] and reg['fields'][short].get('posn') == fdata.get('posn'):
                    alias_fields[fname] = fdata
                    continue
            primary_fields[fname] = fdata

        reg['primary_fields'] = primary_fields
        reg['alias_fields'] = alias_fields
        del reg['fields']

    return registers


def main():
    parser = argparse.ArgumentParser(description="Parse Microchip XC8 device header into JSON")
    parser.add_argument("header", help="Path to .h header file")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    parser.add_argument("--compact", action="store_true", help="Compact JSON output")
    args = parser.parse_args()

    registers = parse_header(args.header)

    indent = None if args.compact else 2
    result = json.dumps(registers, indent=indent)

    if args.output:
        Path(args.output).write_text(result + '\n')
        print(f"Wrote {len(registers)} registers to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()