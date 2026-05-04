# Godot Engine Source Index

**Version:** 4.7.0-beta (from `version.py`)
**Repository Root:** `/home/daelon/projects/library/repos/godot`
**Source Language Breakdown:** ~7599 C/C++/ObjC++ source files, ~131 Python build scripts, ~152 GLSL shaders, ~810 XML doc class files

---

## 1. Top-Level Directory Structure

| Directory | Purpose |
|-----------|---------|
| `core/` | Core types, object system, variants, IO, math, extensions — the foundational layer |
| `scene/` | Scene tree nodes (2D, 3D, GUI, animation, audio, resources), the scene system |
| `servers/` | Headless server singletons: RenderingServer, PhysicsServer2D/3D, AudioServer, DisplayServer, TextServer, XRServer, CameraServer, NavigationServer2D/3D, MovieWriter |
| `editor/` | Full Godot editor — project manager, inspector, dock system, export, import, debugger, shader editor |
| `modules/` | ~60 optional modules (GDScript, Mono/C#, physics backends, navigation, glTF, OpenXR, etc.) — plugged in at build time |
| `drivers/` | Platform/backend drivers: audio, rendering (Vulkan, Metal, D3D12, GLES3), windowing |
| `platform/` | Platform ports: android, ios, linuxbsd, macos, web, windows, visionos |
| `main/` | Application entry point (`main.cpp`), performance tracker, timer sync |
| `doc/` | Class reference XML docs (`doc/classes/*.xml`) and documentation tooling |
| `tests/` | Unit and integration tests |
| `thirdparty/` | ~69 bundled third-party libraries |
| `misc/` | Build utilities, error suppressions, MSVC configs, extension API validation |

### Root-Level Build/Config Files

| File | Purpose |
|------|---------|
| `SConstruct` | SCons entry point; orchestrates entire build |
| `methods.py` | Core SCons helper functions |
| `platform_methods.py` | Platform detection and configuration helpers |
| `version.py` | Version: `major=4, minor=7, patch=0, status="beta"` |
| `gles3_builders.py` | GLES3 shader build rules |
| `glsl_builders.py` | GLSL shader compilation builders |
| `scu_builders.py` | Single Compilation Unit (SCU) build optimization |

---

## 2. Key Entry Points

- **`/main/main.cpp`** — `main()` function. Initializes core types, registers singletons, creates `MainLoop`/`SceneTree`, runs the engine loop.
- **Platform entry points:** `/platform/linuxbsd/godot_linuxbsd.cpp`, `/platform/windows/godot_windows.cpp`, `/platform/macos/godot_main_macos.mm`, `/platform/ios/main_ios.mm`, `/platform/android/java_godot_lib_jni.cpp`, `/platform/web/web_main.cpp`, `/platform/visionos/main_visionos.mm`
- **Type registration:** `/core/register_core_types.cpp` → `/scene/register_scene_types.cpp` → `/servers/register_server_types.cpp` → `/editor/register_editor_types.cpp` → `/modules/register_module_types.h`

---

## 3. Core Module/System Organization (`/core/`)

### `/core/object/` — Object System (the heart of Godot)
- `object.h/cpp` — `Object` base class, properties, signals, groups, notifications
- `class_db.h/cpp` — `ClassDB` — runtime class registration, method binding, property system
- `method_bind.h/cpp` — C++ method binding to GDScript/GDExtension
- `ref_counted.h/cpp` — `RefCounted` — reference-counted base class
- `script_language.h/cpp` — `ScriptLanguage` — abstract base for scripting implementations
- `message_queue.h/cpp` — `MessageQueue` — deferred call queue (call_deferred)
- `callable_mp.h/cpp` — method pointer callables

### `/core/variant/` — Variant Type System
- `variant.h/cpp` — `Variant` — dynamically-typed value container (~40 types)
- `callable.h/cpp` — `Callable` — first-class function references
- `array.h`, `typed_array.h`, `dictionary.h` — collections

### `/core/extension/` — GDExtension System
- `gdextension.h/cpp` — loads/registers native extension libraries
- `gdextension_manager.h/cpp` — singleton managing all loaded extensions
- `gdextension_interface.json` — machine-readable JSON definition of entire GDExtension C interface (~9300 lines)
- `gdextension_interface.cpp` — implementation of all GDExtension function pointers
- `libgodot.h` — `libgodot` API for embedding Godot as a library

### `/core/io/` — Input/Output
Key classes: `FileAccess`, `DirAccess`, `Resource`/`ResourceLoader`/`ResourceSaver`, `Image`/`ImageLoader`, `HTTPClient`, `TCPServer`/`StreamPeer`, `JSON`, `XMLParser`, `ConfigFile`, `PCKPacker`, `TranslationLoaderPO`

### `/core/math/` — Math Types
2D/3D vectors, transforms, AABB, Basis, Quaternion, Color, geometry algorithms (convex hull, triangulation, Delaunay, A*), BVH, expression parser, RNG

### `/core/config/` — `Engine` singleton, `ProjectSettings` singleton

### `/core/input/` — `Input` singleton, `InputMap`, `InputEvent` and subclasses, `Shortcut`

### `/core/string/` — `String`, `StringName`, `NodePath`, `TranslationServer`

### `/core/os/` — `OS` (platform abstraction), `MainLoop`, `Thread`, `Mutex`, `Memory`, `Time`

### `/core/debugger/` — `EngineDebugger`, `RemoteDebugger`, `LocalDebugger`, `ScriptDebugger`

### `/core/crypto/` — `Crypto`, `CryptoCore`, `HashingContext`, `AESContext`

### `/core/templates/` — Container templates: `HashMap`, `HashSet`, `AHashMap`, `List`, `Vector`, `LocalVector`, `RBMap`, `RID`, `RIDOwner`, etc.

---

## 4. Servers (`/servers/`)

All servers are singletons with thread-safe interfaces. GDExtension backends can be plugged in via `*Extension` classes.

| Server | Path | Key Files | Extension Point |
|--------|------|-----------|-----------------|
| RenderingServer | `/servers/rendering/` | `rendering_server.h`, `rendering_device.h`, `rendering_method.h` | RenderingDeviceDriver (Vulkan/Metal/D3D12) |
| PhysicsServer2D | `/servers/physics_2d/` | `physics_server_2d.h` | `PhysicsServer2DExtension` |
| PhysicsServer3D | `/servers/physics_3d/` | `physics_server_3d.h` | `PhysicsServer3DExtension` |
| AudioServer | `/servers/audio/` | `audio_server.h` + ~30 built-in effects | Audio drivers in `/drivers/` |
| DisplayServer | `/servers/display/` | `display_server.h` | Platform-specific in `/platform/*/` |
| TextServer | `/servers/text/` | `text_server.h` | `TextServerExtension` |
| NavigationServer2D/3D | `/servers/navigation_2d/`, `/servers/navigation_3d/` | `navigation_server_*.h` | Implementations in `/modules/` |
| CameraServer | `/servers/camera/` | `camera_server.h` | — |
| XRServer | `/servers/xr/` | `xr_server.h`, `xr_interface.h` | `XRInterfaceExtension` |
| MovieWriter | `/servers/movie_writer/` | `movie_writer.h` | — |

### Rendering Pipeline
```
RenderingServer → RenderingMethod → RendererCompositor
  → forward_clustered (desktop) / forward_mobile (mobile)
    → RendererSceneRenderRD (3D) + RendererCanvasRenderRD (2D)
  RenderingDevice → RenderingDeviceDriver → Vulkan / Metal / D3D12
```

Rendering backend code: `/drivers/vulkan/`, `/drivers/metal/`, `/drivers/d3d12/`, `/drivers/gles3/`

---

## 5. Scene System (`/scene/`)

### `/scene/main/` — Core Scene Framework
`Node`, `SceneTree`, `Viewport`, `Window`, `CanvasItem`, `CanvasLayer`, `MultiplayerAPI`, `Timer`, `HTTPRequest`

### `/scene/2d/` — 2D Nodes
`Node2D`, `Camera2D`, `Light2D`, `Sprite2D`, `AnimatedSprite2D`, `TileMap`/`TileMapLayer`, `CPUParticles2D`, `GPUParticles2D`, `Path2D`/`PathFollow2D`, `Line2D`, `Polygon2D`, `ParallaxBackground`, physics nodes (`CharacterBody2D`, `RigidBody2D`, `StaticBody2D`, `Area2D`), navigation nodes

### `/scene/3d/` — 3D Nodes
`Node3D`, `Camera3D`, `Light3D`, `MeshInstance3D`, `GPUParticles3D`, `Decal`, `FogVolume`, `ReflectionProbe`, `LightmapGI`, `VoxelGI`, `Sprite3D`, `Label3D`, `Path3D`/`PathFollow3D`, `Skeleton3D`, physics nodes, navigation nodes, XR nodes

### `/scene/gui/` — GUI Controls (~130 files)
`Control` (base), `Button`, `Label`, `LineEdit`, `TextEdit`/`CodeEdit`, `Tree`, `ItemList`, `TabBar`/`TabContainer`, `PopupMenu`, `FileDialog`, `ColorPicker`, `SpinBox`, `Slider`, containers (`VBoxContainer`, `HBoxContainer`, `GridContainer`, etc.), `GraphEdit`/`GraphNode`/`GraphFrame`, `RichTextLabel`

### `/scene/animation/` — `AnimationPlayer`, `AnimationTree`, `AnimationMixer`, `Tween`

### `/scene/resources/` — Resource types: `Material`, `Shader`, `Mesh`, `Texture`, `Environment`, `Sky`, `Font`, `Curve`, `Gradient`, `Animation`, `PackedScene`, `MultiMesh`, `NavigationMesh`, etc.

---

## 6. Module Registration Architecture

Each module in `/modules/MODULE_NAME/` must have:
1. **`config.py`** — declares `can_build()`, `configure()`, `is_enabled()`, `get_doc_path()`, `get_doc_classes()`
2. **`register_types.h/cpp`** — `initialize_MODULE()` / `uninitialize_MODULE()` using `ModuleInitializationLevel` (CORE, SERVERS, SCENE, EDITOR)
3. **`SCsub`** — SCons build configuration

### Complete Module List

GDScript, mono (C#), godot_physics_2d, godot_physics_3d, jolt_physics, navigation_2d, navigation_3d, gltf, fbx, openxr, mobile_vr, multiplayer, websocket, webrtc, enet, webxr, visual_shader, csg, gridmap, camera, text_server_adv, text_server_fb, lightmapper_rd, meshoptimizer, regex, jsonrpc, mbedtls, upnp, astcenc, basis_universal, bcdec, betsy, bmp, cvtt, dds, etcpak, hdr, jpg, ktx, msdfgen, png, svg, tga, theora, tinyexr, webp, ogg, vorbis, mp3, interactive_music, xatlas_unwrap, vhacd, raycast, noise, objectdb_profiler, freetype, glslang, accesskit

---

## 7. Editor Architecture (`/editor/`)

- **`editor_node.h/cpp`** — `EditorNode` — main editor window, menu bar, layout, plugin management
- **`editor_interface.h/cpp`** — `EditorInterface` — singleton API for editor plugins
- Subdirectories: `animation/`, `asset_library/`, `audio/`, `debugger/`, `doc/`, `docks/`, `export/`, `file_system/`, `gui/`, `icons/`, `import/`, `inspector/`, `plugins/`, `project_manager/`, `project_upgrade/`, `run/`, `scene/`, `script/`, `settings/`, `shader/`, `themes/`, `translations/`, `version_control/`

---

## 8. GDExtension System

### Key Files
- `/core/extension/gdextension_interface.json` — full API definition (~9300 lines)
- `/core/extension/gdextension.h/cpp` — `GDExtension` class loads/registers native extensions
- `/core/extension/gdextension_manager.h/cpp` — manages extension lifecycle
- `/core/extension/gdextension_library_loader.h/cpp` — loads `.gdextension` config and dynamic library
- `/core/extension/libgodot.h` — `libgodot` API for embedding

### Extension Lifecycle
1. `.gdextension` resource file found by `ResourceLoader`
2. `GDExtensionLibraryLoader` loads dynamic library
3. Library's entry point (`gdextension_init`) called
4. Library registers classes/methods/properties via `GDExtensionInterface` callbacks
5. `GDExtensionManager` tracks init levels: CORE → SERVERS → SCENE → EDITOR

---

## 9. Platform Support

| Platform | Directory | Key Backends |
|----------|-----------|-------------|
| Linux/*BSD | `/platform/linuxbsd/` | Wayland/X11, ALSA/PulseAudio |
| Windows | `/platform/windows/` | D3D12/Vulkan, WASAPI |
| macOS | `/platform/macos/` | Metal/Vulkan, CoreAudio |
| iOS | `/platform/ios/` | Metal |
| Android | `/platform/android/` | OpenSL, Vulkan/GLES |
| Web | `/platform/web/` | WebGL2, WebAudio, WebXR |
| visionOS | `/platform/visionos/` | Metal |

---

## 10. Build System

- **Tool:** SCons (`SConstruct`, `methods.py`, `platform_methods.py`)
- **Python:** >= 3.9, **SCons:** >= 4.0
- Every directory with source files has an `SCsub`
- Module enablement controlled by `/modules/*/config.py` `can_build()` functions
- Build output to `bin/` directory