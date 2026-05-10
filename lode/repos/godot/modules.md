# Module Registration Architecture

Each module in `/modules/MODULE_NAME/` must have:
1. **`config.py`** — declares `can_build()`, `configure()`, `is_enabled()`, `get_doc_path()`, `get_doc_classes()`
2. **`register_types.h/cpp`** — `initialize_MODULE()` / `uninitialize_MODULE()` using `ModuleInitializationLevel` (CORE, SERVERS, SCENE, EDITOR)
3. **`SCsub`** — SCons build configuration

## Complete Module List

GDScript, mono (C#), godot_physics_2d, godot_physics_3d, jolt_physics, navigation_2d, navigation_3d, gltf, fbx, openxr, mobile_vr, multiplayer, websocket, webrtc, enet, webxr, visual_shader, csg, gridmap, camera, text_server_adv, text_server_fb, lightmapper_rd, meshoptimizer, regex, jsonrpc, mbedtls, upnp, astcenc, basis_universal, bcdec, betsy, bmp, cvtt, dds, etcpak, hdr, jpg, ktx, msdfgen, png, svg, tga, theora, tinyexr, webp, ogg, vorbis, mp3, interactive_music, xatlas_unwrap, vhacd, raycast, noise, objectdb_profiler, freetype, glslang, accesskit
