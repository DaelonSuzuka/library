# Godot Engine Source

**Version:** 4.7.0-beta (from `version.py`)
**Repository Root:** `repos/godot`
**Stats:** ~7599 C/C++/ObjC++ source, ~131 Python build scripts, ~152 GLSL shaders, ~810 XML doc class files

## Architecture Overview

```mermaid
graph TD
    main["main/main.cpp"] --> core["core/"]
    main --> scene["scene/"]
    main --> servers["servers/"]
    main --> editor["editor/"]
    core --> object["Object System"]
    core --> variant["Variant Types"]
    core --> extension["GDExtension"]
    scene --> nodes2d["2D Nodes"]
    scene --> nodes3d["3D Nodes"]
    scene --> gui["GUI Controls"]
    servers --> rendering["RenderingServer"]
    servers --> physics["PhysicsServer 2D/3D"]
    servers --> audio["AudioServer"]
    modules["modules/"] --> scene
    modules --> servers
    drivers["drivers/"] --> rendering
    platform["platform/"] --> main
```

## See Also

- [lode-map.md](lode-map.md)
