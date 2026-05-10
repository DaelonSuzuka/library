# Platform Support

| Platform | Directory | Key Backends |
|----------|-----------|-------------|
| Linux/*BSD | `/platform/linuxbsd/` | Wayland/X11, ALSA/PulseAudio |
| Windows | `/platform/windows/` | D3D12/Vulkan, WASAPI |
| macOS | `/platform/macos/` | Metal/Vulkan, CoreAudio |
| iOS | `/platform/ios/` | Metal |
| Android | `/platform/android/` | OpenSL, Vulkan/GLES |
| Web | `/platform/web/` | WebGL2, WebAudio, WebXR |
| visionOS | `/platform/visionos/` | Metal |

## Entry Points

- **`/main/main.cpp`** — `main()`. Initializes core types, registers singletons, creates `MainLoop`/`SceneTree`, runs engine loop.
- Platform-specific: `/platform/linuxbsd/godot_linuxbsd.cpp`, `/platform/windows/godot_windows.cpp`, `/platform/macos/godot_main_macos.mm`, `/platform/ios/main_ios.mm`, `/platform/android/java_godot_lib_jni.cpp`, `/platform/web/web_main.cpp`, `/platform/visionos/main_visionos.mm`

## Build System

- **Tool:** SCons (`SConstruct`, `methods.py`, `platform_methods.py`)
- **Python:** >= 3.9, **SCons:** >= 4.0
- Every directory with source files has an `SCsub`
- Module enablement controlled by `/modules/*/config.py` `can_build()` functions
- Build output to `bin/` directory

### Root Build/Config Files

| File | Purpose |
|------|---------|
| `SConstruct` | SCons entry point; orchestrates entire build |
| `methods.py` | Core SCons helper functions |
| `platform_methods.py` | Platform detection and configuration helpers |
| `version.py` | Version: `major=4, minor=7, patch=0, status="beta"` |
| `gles3_builders.py` | GLES3 shader build rules |
| `glsl_builders.py` | GLSL shader compilation builders |
| `scu_builders.py` | Single Compilation Unit (SCU) build optimization |
