# VS Code Documentation Index

**Repository Root:** `/home/daelon/projects/library/repos/vscode-docs`
**Format:** Markdown built with Docsify
**Primary URL:** https://code.visualstudio.com

---

## 1. Top-Level Structure

| Path | Purpose |
|------|---------|
| `/api/` | Extension API documentation — extensibility reference |
| `/docs/` | User-facing documentation — editor features, languages, debugging, Copilot, remote, enterprise |
| `/learn/` | Structured learning paths (agent foundations, customizations) |
| `/blogs/` | Blog posts by date (`YYYY/MM/DD/slug.md`) |
| `/release-notes/` | Monthly release notes (v0.3.0 through v1.118+) |
| `/remote-release-notes/` | Remote-specific release notes |
| `/remote/` | Advanced containers documentation |
| `/build/` | Build scripts, sidebar generators, keybinding data |
| `/_extensions/` | Custom Sphinx extensions (not directly used — part of docs tooling) |

### Key Config Files

| File | Purpose |
|------|---------|
| `package.json` | npm manifest, dev dependencies (docsify-cli, gulp, husky) |
| `gulpfile.js` |Production build: clones vscode-website, copies content, runs build scripts |
| `index.html` | Docsify config: plugins, sidebar, search, theme |
| `/docs/toc.json` | TOC for user docs |
| `/api/toc.json` | TOC for extension API docs |
| `/learn/toc.json` | TOC for learning paths |

---

## 2. User Documentation (`/docs/`)

### Editor Features

| Topic | Directory | Key Files |
|-------|-----------|-----------|
| Setup/Install | `/docs/setup/` | Linux, macOS, Windows, Web, Raspberry Pi |
| Getting Started | `/docs/getstarted/` | UI, personalize, extensions, tips, Copilot quickstart |
| Editing | `/docs/editing/` | Code basics, IntelliSense, evolved editing, refactoring, snippets |
| Workspaces | `/docs/editing/workspaces/` | Workspaces, multi-root, workspace trust |
| Debug/Test | `/docs/debugtest/` | Tasks, debugging, debug config, testing, port forwarding |
| Source Control | `/docs/sourcecontrol/` | Git overview, staging, branches, merge conflicts, GitHub |
| Terminal | `/docs/terminal/` | Basics, profiles, shell integration, appearance, advanced |
| Configuration | `/docs/configure/` | Settings, keybindings, settings sync, themes, profiles, CLI |
| Accessibility | `/docs/configure/accessibility/` | Accessibility, voice |
| Extensions | `/docs/configure/extensions/` | Marketplace, runtime security |
| Reference | `/docs/reference/` | Default keybindings, default settings, variables, tasks appendix |

### GitHub Copilot (`/docs/copilot/`)
**Top-level:** overview, setup, getting started, smart actions, best practices, troubleshooting, FAQ
**Sub-sections:**
- `concepts/` — language models, context, tools, agents, customization, trust & safety
- `agents/` — agents overview, tutorial, planning, memory, tools, subagents, local/cloud agents
- `chat/` — chat sessions, context, inline chat, review, checkpoints, artifacts, debug view
- `customization/` — instructions, prompt files, custom agents, skills, language models, MCP servers, hooks
- `guides/` — context engineering, TDD, browser agent testing, debugging, monitoring, prompt engineering
- `reference/` — features cheat sheet, settings, MCP config, workspace context

### Remote Development (`/docs/remote/`)
SSH, Dev Containers, WSL, Codespaces, VS Code Server, Tunnels, tutorials, troubleshooting, FAQ

### Dev Containers (`/docs/devcontainers/`)
Containers tutorial, create, attach, advanced, devcontainer.json reference, CLI, tips

### Enterprise (`/docs/enterprise/`)
Policies, AI settings, extensions, telemetry, updates

### Intelligent Apps / AI Toolkit (`/docs/intelligentapps/`)
Overview, Copilot tools, create agents, models, playground, agent builder, evaluation, fine-tuning, tracing

### Language-Specific Docs
| Language | Path |
|----------|------|
| JavaScript | `/docs/nodejs/` |
| TypeScript | `/docs/typescript/` |
| Python | `/docs/python/` |
| Java | `/docs/java/` |
| C++ | `/docs/cpp/` |
| C# | `/docs/csharp/` |
| Language overviews | `/docs/languages/` |

### Other
- **Data Science:** `/docs/datascience/` (Jupyter, PyTorch, data wrangler)
- **Azure:** `/docs/azure/`
- **Container Tools:** `/docs/containers/`

---

## 3. Extension API Documentation (`/api/`)

### Get Started (`/api/get-started/`)
Your first extension, extension anatomy, wrapping up

### Extension Capabilities (`/api/extension-capabilities/`)
Overview, common capabilities, theming, extending workbench

### Extension Guides (`/api/extension-guides/`)
**Core:** command, color theme, file icon theme, product icon theme, tree view, webview, notebook, custom editors, virtual documents, virtual workspaces, web extensions, workspace trust, task provider, SCM provider, debugger extension, markdown extension, testing, custom data, telemetry

**AI (`/api/extension-guides/ai/`):** extensibility overview, chat participant, chat tutorial, tools (LM), MCP, language model, LM tutorial, LM chat provider, prompt-tsx

### UX Guidelines (`/api/ux-guidelines/`)
Overview + 14 specific pages (activity bar, sidebars, panel, status bar, views, editor actions, quick picks, command palette, notifications, webviews, context menus, walkthroughs, settings)

### Language Extensions (`/api/language-extensions/`)
Overview, syntax highlighting (TextMate), semantic highlighting, snippets, language configuration, programmatic features, LSP extension guide, embedded languages

### Testing & Publishing (`/api/working-with-extensions/`)
Testing, publishing (vsce, VSIX), bundling (webpack/esbuild), CI

### Advanced Topics (`/api/advanced-topics/`)
Extension host, remote extensions, proposed API, TSLint→ESLint migration, Python extension template

---

## 4. API Reference (`/api/references/`)

| File | Content |
|------|---------|
| `vscode-api.template` | Template for VS Code API page (content generated from `vscode.d.ts`) |
| `contribution-points.md` | All `contributes.*` fields in package.json (34 points, 1644 lines) |
| `activation-events.md` | All `activationEvents` entries (377 lines) |
| `extension-manifest.md` | All package.json fields for extensions (317 lines) |
| `commands.md` | Built-in commands reference (531 lines) |
| `theme-color.md` | Theme color reference — all `workbench.colorCustomizations` keys (1341 lines) |
| `when-clause-contexts.md` | When clause context keys (344 lines) |
| `icons-in-labels.md` | Product icon reference / Codicon IDs (838 lines) |
| `document-selector.md` | Document selector filtering (98 lines) |

---

## 5. Contribution Points (34 total)

`authentication`, `breakpoints`, `chatInstructions`, `chatPromptFiles`, `colors`, `commands`, `configuration`, `configurationDefaults`, `customEditors`, `debuggers`, `grammars`, `icons`, `iconThemes`, `jsonValidation`, `keybindings`, `languages`, `menus`, `problemMatchers`, `problemPatterns`, `productIconThemes`, `resourceLabelFormatters`, `semanticTokenModifiers`, `semanticTokenScopes`, `semanticTokenTypes`, `snippets`, `submenus`, `taskDefinitions`, `terminal`, `themes`, `typescriptServerPlugins`, `views`, `viewsContainers`, `viewsWelcome`, `walkthroughs`

---

## 6. Build/Publishing

- **Local preview:** `npm run serve` → `npm run generate-sidebar && docsify serve .`
- **Sidebar generation:** `node build/generate-sidebar.js` reads TOC JSONs + frontmatter
- **Production build:** `gulp build-dist` — clones vscode-website, copies content, runs scripts
- **CI:** Azure Pipelines

---

## Quick-Reference: Topic → Path

| Topic | Path |
|-------|------|
| First extension | `/api/get-started/your-first-extension.md` |
| Extension anatomy | `/api/get-started/extension-anatomy.md` |
| Capabilities overview | `/api/extension-capabilities/overview.md` |
| Commands API | `/api/extension-guides/command.md` |
| Webview API | `/api/extension-guides/webview.md` |
| Notebook API | `/api/extension-guides/notebook.md` |
| Debugger (DAP) | `/api/extension-guides/debugger-extension.md` |
| AI — Chat | `/api/extension-guides/ai/chat.md` |
| AI — LM Tool | `/api/extension-guides/ai/tools.md` |
| AI — MCP | `/api/extension-guides/ai/mcp.md` |
| All contribution points | `/api/references/contribution-points.md` |
| All activation events | `/api/references/activation-events.md` |
| Extension manifest | `/api/references/extension-manifest.md` |
| Built-in commands | `/api/references/commands.md` |
| Theme colors | `/api/references/theme-color.md` |
| When clause contexts | `/api/references/when-clause-contexts.md` |
| Icons (Codicons) | `/api/references/icons-in-labels.md` |
| Publishing extensions | `/api/working-with-extensions/publishing-extension.md` |
| Bundling | `/api/working-with-extensions/bundling-extension.md` |
| Testing extensions | `/api/working-with-extensions/testing-extension.md` |
| LSP extension guide | `/api/language-extensions/language-server-extension-guide.md` |
| Copilot user docs | `/docs/copilot/overview.md` |
| Copilot agents | `/docs/copilot/agents/overview.md` |
| Copilot customization | `/docs/copilot/customization/overview.md` |
| Dev Containers | `/docs/devcontainers/containers.md` |
| Remote SSH | `/docs/remote/ssh.md` |
| Terminal | `/docs/terminal/basics.md` |
| Debugging | `/docs/debugtest/debugging.md` |