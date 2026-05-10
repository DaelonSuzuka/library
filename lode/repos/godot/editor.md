# Editor Architecture (`/editor/`)

- **`editor_node.h/cpp`** — `EditorNode` — main editor window, menu bar, layout, plugin management
- **`editor_interface.h/cpp`** — `EditorInterface` — singleton API for editor plugins

## Subdirectories

| Path | Purpose |
|------|---------|
| `animation/` | Animation editing tools |
| `asset_library/` | Asset library integration |
| `audio/` | Audio bus editor |
| `debugger/` | Script/object debugger panels |
| `doc/` | Documentation tooling |
| `docks/` | FileSystem, Inspector, Scene tree docks |
| `export/` | Platform export managers |
| `file_system/` | FileSystem dock |
| `gui/` | Editor-specific GUI components |
| `icons/` | SVG editor icons |
| `import/` | Resource import pipeline |
| `inspector/` | Property inspector |
| `plugins/` | Editor plugin framework |
| `project_manager/` | Project list/creation |
| `project_upgrade/` | Project version migration |
| `run/` | Play/stop controls |
| `scene/` | Scene editor |
| `script/` | Script editor |
| `settings/` | Editor settings |
| `shader/` | Shader editor |
| `themes/` | Editor themes |
| `translations/` | Editor i18n |
| `version_control/` | VCS integration |
