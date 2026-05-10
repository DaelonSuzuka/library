# VS Code Documentation

**Repository Root:** `repos/vscode-docs`
**Format:** Markdown built with Docsify
**URL:** https://code.visualstudio.com

## Top-Level Structure

| Path | Purpose |
|------|---------|
| `/api/` | Extension API documentation |
| `/docs/` | User-facing documentation |
| `/learn/` | Structured learning paths |
| `/blogs/` | Blog posts |
| `/release-notes/` | Monthly release notes |

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
| Theme colors | `/api/references/theme-color.md` |
| When clause contexts | `/api/references/when-clause-contexts.md` |
| Icons (Codicons) | `/api/references/icons-in-labels.md` |
| Publishing extensions | `/api/working-with-extensions/publishing-extension.md` |
| LSP extension guide | `/api/language-extensions/language-server-extension-guide.md` |
| Copilot user docs | `/docs/copilot/overview.md` |
| Copilot agents | `/docs/copilot/agents/overview.md` |
| Copilot customization | `/docs/copilot/customization/overview.md` |
| Dev Containers | `/docs/devcontainers/containers.md` |
| Remote SSH | `/docs/remote/ssh.md` |
| Terminal | `/docs/terminal/basics.md` |
| Debugging | `/docs/debugtest/debugging.md` |

## Build

- Local: `npm run serve` → `npm run generate-sidebar && docsify serve .`
- Production: `gulp build-dist`
- Sidebar: `node build/generate-sidebar.js` reads TOC JSONs

## Deep Index

See [lode-map.md](lode-map.md) for a complete file-level path index covering API guides, user docs, Copilot docs, and all learning modules.

## See Also

- [lode-map.md](lode-map.md)
