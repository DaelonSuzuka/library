# Core Module (`/core/`)

## Object System (`/core/object/`)
- `object.h/cpp` — `Object` base class, properties, signals, groups, notifications
- `class_db.h/cpp` — `ClassDB` — runtime class registration, method binding, property system
- `method_bind.h/cpp` — C++ method binding to GDScript/GDExtension
- `ref_counted.h/cpp` — `RefCounted` — reference-counted base class
- `script_language.h/cpp` — `ScriptLanguage` — abstract base for scripting implementations
- `message_queue.h/cpp` — `MessageQueue` — deferred call queue (call_deferred)
- `callable_mp.h/cpp` — method pointer callables

## Variant Type System (`/core/variant/`)
- `variant.h/cpp` — `Variant` — dynamically-typed value container (~40 types)
- `callable.h/cpp` — `Callable` — first-class function references
- `array.h`, `typed_array.h`, `dictionary.h` — collections

## GDExtension (`/core/extension/`)
See [gdextension.md](gdextension.md).

## Input/Output (`/core/io/`)
`FileAccess`, `DirAccess`, `Resource`/`ResourceLoader`/`ResourceSaver`, `Image`/`ImageLoader`, `HTTPClient`, `TCPServer`/`StreamPeer`, `JSON`, `XMLParser`, `ConfigFile`, `PCKPacker`, `TranslationLoaderPO`

## Math (`/core/math/`)
2D/3D vectors, transforms, AABB, Basis, Quaternion, Color, geometry algorithms (convex hull, triangulation, Delaunay, A*), BVH, expression parser, RNG

## Other Core Subdirectories
| Path | Contents |
|------|----------|
| `/core/config/` | `Engine` singleton, `ProjectSettings` singleton |
| `/core/input/` | `Input` singleton, `InputMap`, `InputEvent` and subclasses, `Shortcut` |
| `/core/string/` | `String`, `StringName`, `NodePath`, `TranslationServer` |
| `/core/os/` | `OS` (platform abstraction), `MainLoop`, `Thread`, `Mutex`, `Memory`, `Time` |
| `/core/debugger/` | `EngineDebugger`, `RemoteDebugger`, `LocalDebugger`, `ScriptDebugger` |
| `/core/crypto/` | `Crypto`, `CryptoCore`, `HashingContext`, `AESContext` |
| `/core/templates/` | `HashMap`, `HashSet`, `AHashMap`, `List`, `Vector`, `LocalVector`, `RBMap`, `RID`, `RIDOwner` |

## Entry Points
- Type registration: `/core/register_core_types.cpp` → `/scene/register_scene_types.cpp` → `/servers/register_server_types.cpp` → `/editor/register_editor_types.cpp` → `/modules/register_module_types.h`
