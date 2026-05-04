# Godot Documentation Index

**Repository Root:** `/home/daelon/projects/library/repos/godot-docs`
**Format:** reStructuredText (reST) built with Sphinx
**License:** CC BY 3.0 (manual), MIT (classes/)

---

## 1. Top-Level Structure

| Path | Purpose |
|------|---------|
| `/about/` | Introduction, features, FAQ, system requirements, release policy, changelog |
| `/getting_started/` | Onboarding: intro, step-by-step, first 2D game, first 3D game |
| `/tutorials/` | Main manual: topic-organized tutorials |
| `/engine_details/` | Engine internals: architecture, API, C++ development, editor dev, file formats |
| `/classes/` | Auto-generated class reference (~1070+ `.rst` files, one per class) |
| `/community/` | Asset library, channels, external tutorials |
| `/img/` | Shared images |
| `/_extensions/` | Custom Sphinx extensions (gdscript lexer, godot_descriptions, override_jobs) |
| `/_static/` | CSS, JS, redirects |
| `/_tools/` | Build/tooling scripts (codespell, RST checker, redirect tools) |
| `/conf.py` | Sphinx build configuration |

---

## 2. Documentation Sections

### Getting Started (`/getting_started/`)
- **Introduction:** What is Godot, design philosophy, key concepts, editor tour, learn to code with GDScript
- **Step by Step:** Nodes & scenes, instancing, scripting, player input, signals
- **First 2D Game:** 7-part tutorial (project setup → finishing)
- **First 3D Game:** 9-part tutorial (setup → animations → going further)

### Tutorials by Topic (`/tutorials/`)

| Topic | Path | Key Files |
|-------|------|-----------|
| 2D | `/tutorials/2d/` | Canvas layers, transforms, lights, sprites, particles, tilemaps, antialiasing, parallax |
| 3D | `/tutorials/3d/` | Transforms, StandardMaterial3D, lights, decals, HDR, volumetric fog, occlusion, GI |
| Animation | `/tutorials/animation/` | AnimationPlayer, AnimationTree, cutout animation, videos, movies |
| Assets Pipeline | `/tutorials/assets_pipeline/` | Import process, images, audio, translations, 3D scene import/export |
| Audio | `/tutorials/audio/` | Buses, effects, streams, sync, microphone, TTS |
| Best Practices | `/tutorials/best_practices/` | Scene organization, scenes vs scripts, autoloads, data patterns, VCS |
| Editor | `/tutorials/editor/` | CLI, customization, key mapping, project manager, project settings |
| Export | `/tutorials/export/` | Per-platform export (Android, iOS, Linux, macOS, Windows, Web, visionOS, servers) |
| I18n | `/tutorials/i18n/` | Internationalization, Gettext, spreadsheets, pseudolocalization |
| Inputs | `/tutorials/inputs/` | InputEvent, gamepads, mouse, custom cursor, quit handling |
| IO | `/tutorials/io/` | Data paths, filesystem, save games, binary serialization, background loading |
| Math | `/tutorials/math/` | Vectors, matrices, transforms, interpolation, bezier curves, RNG |
| Migrating | `/tutorials/migrating/` | Upgrading guides: 3→4, 4.0→4.1, ... 4.5→4.6 |
| Navigation | `/tutorials/navigation/` | NavMesh, agents, layers, links, obstacles, servers, pathfinding |
| Networking | `/tutorials/networking/` | High-level multiplayer, HTTPClient, WebSocket, WebRTC, SSL |
| Performance | `/tutorials/performance/` | CPU/GPU optimization, thread safety, MultiMesh, multithreading, server APIs |
| Physics | `/tutorials/physics/` | RigidBody, CharacterBody2D, collision shapes, ray casting, ragdolls, interpolation |
| Platform | `/tutorials/platform/` | Android plugins, iOS plugins, web shell/JS bridge |
| Plugins | `/tutorials/plugins/` | `@tool` scripts, editor plugins (gizmos, import, inspector, visual shader) |
| Rendering | `/tutorials/rendering/` | Renderer comparison, viewports, multiple resolutions, compositor, HDR output |
| Scripting | `/tutorials/scripting/` | See scripting sub-sections below |
| Shaders | `/tutorials/shaders/` | Intro, first shaders, compute shaders, visual shaders, full shader language reference |
| UI | `/tutorials/ui/` | Size/anchors, containers, custom controls, navigation/focus, skinning, fonts, theme editor |
| XR | `/tutorials/xr/` | Setup, terminology, action map, locomotion, OpenXR, hand tracking, body tracking |

### Scripting (`/tutorials/scripting/`)

**Language-agnostic:** how to read API, debug, idle vs physics processing, groups, nodes, signals, resources, autoload, scene tree, logging

**GDScript (`/tutorials/scripting/gdscript/`):** basics, advanced, exports, documentation comments, style guide, static typing, warnings, format strings

**C# / .NET (`/tutorials/scripting/c_sharp/`):** basics, features, style guide, differences, collections, Variant, signals, exports, global classes, 22 diagnostics (GD0001–GD0402)

**C++ / GDExtension (`/tutorials/scripting/cpp/`):** about godot-cpp, example project, core types, build systems (SCons, CMake)

### Engine Details (`/engine_details/`)
- **Architecture:** Engine internals, core types, class tree
- **Engine API:** C++ custom modules, GDExtension C++ example, core types, build system
- **Development:** Compiling, IDE config, debugging, profiling
- **Editor:** Editor development
- **Class Reference:** How to write/contribute class reference docs
- **File Formats:** `.tscn` file format spec

---

## 3. Class Reference

**Location:** `/classes/` — ~1070+ RST files
**Naming:** `class_<lowercaseclassname>.rst` (e.g., `class_node.rst`)
**Source:** Auto-generated from engine's `doc/classes/*.xml`

**Categories in `index.rst`:**
- **Globals:** `@GDScript`, `@GlobalScope`
- **Nodes:** All engine nodes (~300+)
- **Resources:** All resource types (~400+)
- **Other Objects:** Singletons, servers, utility classes (~300+)
- **Editor-Only:** ~80 entries
- **Variant Types:** Built-in types (int, float, String, Vector2, Vector3, Color, Dictionary, Array, etc.)

---

## 4. Build System

- **Builder:** Sphinx >= 8.1, Python 3.11
- **Theme:** `sphinx_rtd_theme`
- **Custom extensions:** `gdscript` (Pygments lexer), `godot_descriptions`, `override_jobs`
- **Build:** `make html` (default), `make gettext` (translations)
- **CI:** GitHub Actions — sync class ref from engine, build offline docs, check URLs

---

## 5. Localization

14 languages: en, de, es, fr, fi, it, ja, ko, pl, pt_BR, ru, uk, zh_Hans, zh_Hant
Translations in separate `godot-docs-l10n` repo, managed via Weblate

---

## Quick-Reference: Topic → Path

| Topic | Path |
|-------|------|
| GDScript language | `/tutorials/scripting/gdscript/` |
| C#/.NET scripting | `/tutorials/scripting/c_sharp/` |
| C++ (GDExtension) | `/tutorials/scripting/cpp/` |
| Scenes & nodes | `/getting_started/step_by_step/nodes_and_scenes.rst` |
| Signals | `/getting_started/step_by_step/signals.rst` |
| 2D rendering | `/tutorials/2d/` |
| 3D rendering | `/tutorials/3d/` |
| Shaders | `/tutorials/shaders/` |
| Shader language ref | `/tutorials/shaders/shader_reference/shading_language.rst` |
| Physics | `/tutorials/physics/` |
| UI / GUI | `/tutorials/ui/` |
| Networking | `/tutorials/networking/` |
| Audio | `/tutorials/audio/` |
| Animation | `/tutorials/animation/` |
| Input | `/tutorials/inputs/` |
| Navigation | `/tutorials/navigation/` |
| XR / VR | `/tutorials/xr/` |
| Export / Platforms | `/tutorials/export/` |
| Performance | `/tutorials/performance/` |
| Engine architecture | `/engine_details/architecture/` |
| Class API lookup | `/classes/class_<name>.rst` |
| Migration guides | `/tutorials/migrating/` |