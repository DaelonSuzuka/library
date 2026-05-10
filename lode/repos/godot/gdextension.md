# GDExtension System

## Key Files

| File | Purpose |
|------|---------|
| `/core/extension/gdextension_interface.json` | Full API definition (~9300 lines) |
| `/core/extension/gdextension.h/cpp` | `GDExtension` class loads/registers native extensions |
| `/core/extension/gdextension_manager.h/cpp` | Manages extension lifecycle |
| `/core/extension/gdextension_library_loader.h/cpp` | Loads `.gdextension` config and dynamic library |
| `/core/extension/libgodot.h` | `libgodot` API for embedding |

## Extension Lifecycle

1. `.gdextension` resource file found by `ResourceLoader`
2. `GDExtensionLibraryLoader` loads dynamic library
3. Library's entry point (`gdextension_init`) called
4. Library registers classes/methods/properties via `GDExtensionInterface` callbacks
5. `GDExtensionManager` tracks init levels: CORE → SERVERS → SCENE → EDITOR
