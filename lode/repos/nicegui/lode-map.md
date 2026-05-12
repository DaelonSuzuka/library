# NiceGUI — Lode Map

```
lode/repos/nicegui/
├── summary.md           # overview, architecture, element hierarchy, element/function catalog
├── lode-map.md           # this file
└── custom-behavior.md    # 8 mechanisms for customizing/extending elements
```

## Package Structure: `nicegui/`

```
nicegui/
├── __init__.py               # Exports: App, Client, ElementFilter, Event, ui, binding, etc.
├── ui.py                     # Lazy-import facade (130+ names — primary public API)
├── nicegui.py                # App singleton: startup, shutdown, routes
├── element.py                # Element base class (extends Visibility)
├── client.py                 # Client per browser session
├── page.py                   # @page decorator and Page class
├── binding.py                # Data binding: bind, bind_from, bind_to
├── context.py                # Page/slot context stacks
├── core.py                   # Core event loop
├── event.py / events.py     # Event system
├── outbox.py                 # Batches DOM mutations → Socket.IO
├── storage.py                # Per-user/app/secret storage
├── observables.py            # ObservableDict, ObservableList
├── run.py / ui_run.py        # ui.run() implementation
├── api_router.py             # APIRouter for sub-apps
├── background_tasks.py       # Background task management
├── language.py / translations.py  # i18n
├── slot.py                   # Vue slot concept
├── defaults.py               # Default configuration
├── dependencies.py           # JS/CSS dependency registration
├── props.py / classes.py / style.py  # Quasar attribute helpers
├── favicon.py                # Favicon handling
├── timer.py                  # ui.timer periodic execution
├── version.py                # __version__
├── app/                      # App module
│   ├── app.py                # App class (startup, shutdown, routes)
│   ├── app_config.py         # AppConfig (title, viewport)
│   └── range_response.py     # HTTP range responses
├── elements/                 # 90+ UI elements (see summary.md)
│   ├── mixins/               # 14 mixin classes
│   ├── aggrid/               # AG Grid (JS bundle)
│   ├── anywidget/            # Jupyter AnyWidget
│   ├── codemirror/           # CodeMirror editor (JS bundle)
│   ├── echart/               # ECharts (JS bundle)
│   ├── joystick/             # Virtual joystick (JS bundle)
│   ├── json_editor/          # JSON editor (JS bundle)
│   ├── leaflet/              # Leaflet maps (JS bundle)
│   ├── mermaid/              # Mermaid diagrams (JS bundle)
│   ├── plotly/               # Plotly charts (JS bundle)
│   ├── scene/                # Three.js 3D scene (JS bundle)
│   ├── sortable/             # Sortable.js (JS bundle)
│   └── xterm/                # Terminal emulator (JS bundle)
├── functions/                # Non-element UI functions
│   ├── clipboard.py, download.py, html.py, javascript.py
│   ├── navigate.py, notify.py, on.py, on_exception.py
│   ├── page_title.py, refreshable.py, status_code.py
│   ├── style.py, update.py
├── helpers/                  # Internal utilities
├── json/                     # JSON serialization (orjson wrapper)
├── native/                   # Native desktop mode (pywebview)
├── persistence/              # Storage backends (file, Redis)
├── static/                   # Vue, Quasar, Socket.IO, Tailwind, fonts
├── templates/                # index.html (Vue/Quasar shell)
└── testing/                  # Test utilities (Screen, User simulation)
```

## Examples (59 projects)

| Example | Path | Description |
|---------|------|-------------|
| 3D Scene | `examples/3d_scene/` | Three.js scene |
| AI Interface | `examples/ai_interface/` | AI chat interface |
| API Requests | `examples/api_requests/` | HTTP API calls |
| Audio Recorder | `examples/audio_recorder/` | Custom audio recording |
| Authentication | `examples/authentication/` | User auth flow |
| Chat App | `examples/chat_app/` | Realtime chat |
| Chat with AI | `examples/chat_with_ai/` | AI-powered chat |
| Custom Binding | `examples/custom_binding/` | Data binding patterns |
| Custom Vue Component | `examples/custom_vue_component/` | Vue.js integration |
| Descope Auth | `examples/descope_auth/` | Descope OAuth |
| Device Control | `examples/device_control/` | IoT/lightbulb control |
| Docker | `examples/docker_image/` | Containerized deployment |
| Download Text | `examples/download_text_as_file/` | File download |
| Editable AG Grid | `examples/editable_ag_grid/` | Editable data table |
| Editable Table | `examples/editable_table/` | QTable editing |
| FastAPI | `examples/fastapi/` | FastAPI integration |
| FFmpeg | `examples/ffmpeg_extract_images/` | Video frame extraction |
| FullCalendar | `examples/fullcalendar/` | Calendar component |
| Generate PDF | `examples/generate_pdf/` | PDF generation |
| Global Worker | `examples/global_worker/` | Background workers |
| Google OAuth | `examples/google_oauth2/` | OAuth2 flow |
| Google One Tap | `examples/google_one_tap_auth/` | One-tap auth |
| Image Mask | `examples/image_mask_overlay/` | Image overlay |
| Infinite Scroll | `examples/infinite_scroll/` | Scroll pagination |
| Lightbox | `examples/lightbox/` | Image lightbox |
| Local File Picker | `examples/local_file_picker/` | Server-side file browser |
| Menu & Tabs | `examples/menu_and_tabs/` | Navigation pattern |
| Modularization | `examples/modularization/` | App structure pattern |
| nginx HTTPS | `examples/nginx_https/` | HTTPS reverse proxy |
| nginx Subpath | `examples/nginx_subpath/` | Subpath deployment |
| Node Module | `examples/node_module_integration/` | NPM integration |
| OpenAI Assistant | `examples/openai_assistant/` | OpenAI integration |
| OpenCV Webcam | `examples/opencv_webcam/` | Webcam streaming |
| Pandas DataFrame | `examples/pandas_dataframe/` | Data display |
| Progress | `examples/progress/` | Progress bars |
| PySerial | `examples/pyserial/` | Serial port I/O |
| Pytests | `examples/pytests/` | Testing pattern |
| Reaktiv | `examples/reaktiv/` | Reactive programming |
| Redis Storage | `examples/redis_storage/` | Redis persistence |
| ROS2 | `examples/ros2/` | Robot OS integration |
| Script Executor | `examples/script_executor/` | Run external scripts |
| Search as You Type | `examples/search_as_you_type/` | Live search |
| Signature Pad | `examples/signature_pad/` | Custom signature component |
| SimPy | `examples/simpy/` | Discrete event simulation |
| SPA | `examples/single_page_app/` | Single-page routing |
| Slideshow | `examples/slideshow/` | Image slideshow |
| Slots | `examples/slots/` | Quasar slot usage |
| SQLite | `examples/sqlite_database/` | Database integration |
| Stripe | `examples/stripe/` | Payment integration |
| SVG Clock | `examples/svg_clock/` | SVG animation |
| Table & Slots | `examples/table_and_slots/` | Table customization |
| Threaded NiceGUI | `examples/threaded_nicegui/` | Threading pattern |
| Todo List | `examples/todo_list/` | CRUD todo app |
| Trello Cards | `examples/trello_cards/` | Drag-and-drop cards |
| Vue Vite | `examples/vue_vite/` | Vite-based Vue component |
| WebSerial | `examples/webserial/` | Browser serial port |
| WebSockets | `examples/websockets/` | WebSocket comms |
| xterm | `examples/xterm/` | Terminal emulator |
| ZeroMQ | `examples/zeromq/` | ZMQ messaging |

## Tests (110+ files)

`tests/` — one test file per element/feature. Pytest fixtures in `conftest.py`. Test helpers: `Screen` (Selenium), `User` (simulation without browser).

## Website/Documentation

`website/` — NiceGUI-powered documentation site with:
- `documentation/content/` — 80+ element/feature documentation pages (Python, each with live demos)
- `documentation/` system: code extraction, demo rendering, API reference generation, full-text search
- Organized into sections: Foundations, Controls, Data Elements, Page Layout, Action/Events, Styling, Pages/Routing, Audiovisual, Text, Security, Testing, Config/Deployment, Binding