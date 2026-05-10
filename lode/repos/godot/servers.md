# Servers (`/servers/`)

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

## Rendering Pipeline

```
RenderingServer → RenderingMethod → RendererCompositor
  → forward_clustered (desktop) / forward_mobile (mobile)
    → RendererSceneRenderRD (3D) + RendererCanvasRenderRD (2D)
  RenderingDevice → RenderingDeviceDriver → Vulkan / Metal / D3D12
```

Rendering backend code: `/drivers/vulkan/`, `/drivers/metal/`, `/drivers/d3d12/`, `/drivers/gles3/`
