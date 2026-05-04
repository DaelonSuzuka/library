# VS Code Extension Samples Index

**Repository Root:** `/home/daelon/projects/library/repos/vscode-extension-samples`
**Organization:** Each sample is a standalone extension in its own top-level directory (81 samples total)
**VS Code API Target:** `^1.100.0` (most samples)
**Build:** TypeScript (`tsc`), some use webpack or esbuild

---

## Sample Organization

- **Base template:** `.base-sample/` — canonical scaffold (package.json, tsconfig, eslint.config.mjs, .vscode/ launch+tasks)
- **Master registry:** `.scripts/samples.ts` — `samples[]` and `lspSamples[]` with description, path, guide link, APIs, contributions
- **Root scripts:** `compile-all`, `lint-all`, `install-all`, `audit-fix-all`, `format-all`, `update-readme`, `validate`

---

## Complete Sample Index (by API/Feature)

### Getting Started
| Sample | APIs / Feature |
|--------|---------------|
| `helloworld-sample` | `commands.registerCommand`, `window.showInformationMessage` |
| `helloworld-minimal-sample` | Same, plain JavaScript (no compilation) |
| `helloworld-test-sample` | Same, with `vscode-test` integration tests |
| `helloworld-test-cli-sample` | Same, with `@vscode/test-cli` + `@vscode/test-electron` |
| `helloworld-web-sample` | Same, VS Code Web extension (webpack, browser entry) |

### Bundling
| Sample | Feature |
|--------|---------|
| `webpack-sample` | Webpack bundling |
| `esbuild-sample` | esbuild bundling |

### Language Features
| Sample | APIs / Feature |
|--------|---------------|
| `completions-sample` | `languages.registerCompletionItemProvider`, CompletionItem, SnippetString |
| `code-actions-sample` | `languages.registerCodeActionsProvider`, CodeActionProvider |
| `codelens-sample` | `languages.registerCodeLensProvider`, CodeLens |
| `call-hierarchy-sample` | CallHierarchyProvider, CallHierarchyItem |
| `inline-completions` | Inline completion provider (proposed API) |
| `semantic-tokens-sample` | `languages.registerDocumentSemanticTokensProvider` |
| `diagnostic-related-information-sample` | Diagnostic, DiagnosticRelatedInformation |
| `snippet-sample` | Contributing snippets (contribution-only) |
| `language-configuration-sample` | Language configuration (contribution-only) |

### Language Server Protocol (LSP)
| Sample | Feature |
|--------|---------|
| `lsp-sample` | Canonical LSP client + server |
| `lsp-log-streaming-sample` | LSP with JSON log streaming |
| `lsp-multi-server-sample` | LSP with one server per workspace folder |
| `lsp-web-extension-sample` | LSP running in browser (webpack) |
| `lsp-user-input-sample` | LSP with code actions using UI (QuickPick/InputBox) |
| `lsp-embedded-language-service` | LSP for embedded languages (HTML+CSS) |
| `lsp-embedded-request-forwarding` | LSP embedded language support via request forwarding |
| `wasm-language-server` | WASM-based language server |

### Editor Features
| Sample | APIs / Feature |
|--------|---------------|
| `document-editing-sample` | TextEditor.edit, TextDocument.getText |
| `decorator-sample` | TextEditor.setDecorations, DecorationTypes |
| `contentprovider-sample` | TextDocumentContentProvider (virtual documents) |
| `virtual-document-sample` | Virtual documents (cowsay scheme) |
| `document-paste` | Document paste edit API (proposed) |
| `drop-on-document` | Document on drop API (proposed) |

### UI & Views
| Sample | APIs / Feature |
|--------|---------------|
| `webview-sample` | `window.createWebviewPanel`, `window.registerWebviewPanelSerializer` |
| `webview-view-sample` | `window.registerWebviewViewProvider` (sidebar webview) |
| `webview-codicons-sample` | Codicons in webviews |
| `tree-view-sample` | `window.createTreeView`, TreeDataProvider, 5 views |
| `statusbar-sample` | `window.createStatusBarItem` |
| `progress-sample` | `window.withProgress` |
| `quickinput-sample` | QuickPick, InputBox, multi-step input |
| `notifications-sample` | Info/warning/error/modal/progress notifications |
| `welcome-view-content-sample` | Views Welcome content |
| `tabs-api-sample` | Tabs API (close inactive tabs) |

### Configuration & Settings
| Sample | APIs / Feature |
|--------|---------------|
| `configuration-sample` | `workspace.getConfiguration`, `workspace.onDidChangeConfiguration` |
| `l10n-sample` | `vscode.l10n.t()`, `package.nls.json`, Japanese translation |

### Authentication & Security
| Sample | APIs / Feature |
|--------|---------------|
| `authenticationprovider-sample` | `authentication.registerAuthenticationProvider` (Azure DevOps PAT) |
| `github-authentication-sample` | Using built-in GitHub auth provider |

### Terminal
| Sample | APIs / Feature |
|--------|---------------|
| `terminal-sample` | `window.createTerminal`, Terminal events, terminal profiles |
| `extension-terminal-sample` | Pseudoterminal (extension-backed terminal) |
| `shell-integration-sample` | Shell integration API |

### File System
| Sample | APIs / Feature |
|--------|---------------|
| `fsprovider-sample` | `workspace.registerFileSystemProvider` (memfs) |
| `fsconsumer-sample` | `workspace.fs` (reading/writing files) |
| `nodefs-provider-sample` | FileSystemProvider backed by Node.js fs |

### Source Control, Comments, editors
| Sample | Feature |
|--------|---------|
| `source-control-sample` | SCM provider (JS Fiddle) |
| `comment-sample` | Commenting API (threads, drafts, replies) |
| `custom-editor-sample` | CustomTextEditorProvider (binary/text editors) |

### Notebooks
| Sample | Feature |
|--------|---------|
| `notebook-serializer-sample` | Notebook serializer + controller |
| `notebook-renderer-sample` | Custom notebook output renderer (plain JS) |
| `notebook-renderer-react-sample` | Notebook renderer with React |
| `notebook-extend-markdown-renderer-sample` | Extending built-in markdown renderer |
| `notebook-format-code-action-sample` | Code actions for notebook cells |
| `jupyter-kernel-execution-sample` | Jupyter kernel execution |
| `jupyter-server-provider-sample` | Jupyter server provider |

### Chat & AI
| Sample | Feature |
|--------|---------|
| `chat-sample` | Chat participant + LM API + Tools (3 participants, 3 tools) |
| `chat-tutorial` | Beginner chat participant (@tutor) |
| `chat-model-provider-sample` | Custom chat model provider |
| `chat-output-renderer-sample` | Custom chat output renderer (Mermaid) |
| `chat-context-sample` | Chat context provider |
| `lm-api-tutorial` | Language Model API tutorial |
| `mcp-extension-sample` | MCP server connection API (proposed) |

### Testing, tasks, more
| Sample | Feature |
|--------|---------|
| `test-provider-sample` | Test explorer/provider API |
| `task-provider-sample` | Custom task provider (Rake + build scripts) |
| `basic-multi-root-sample` | Multi-root workspace API |
| `uri-handler-sample` | `vscode://` URI handler |
| `telemetry-sample` | Telemetry API |
| `getting-started-sample` | Walkthrough / Getting Started page |

### Themes & Icons
| Sample | Feature |
|--------|---------|
| `theme-sample` | Color theme contribution |
| `product-icon-theme-sample` | Product icon theme contribution |
| `custom-data-sample` | Custom HTML/CSS data (contribution-only) |

### Vim & Proposed API
| Sample | Feature |
|--------|---------|
| `vim-sample` | Multi-API demo (simplified Vim emulation) |
| `proposed-api-sample` | How to use proposed APIs (template) |

### WebAssembly
| Sample | Feature |
|--------|---------|
| `wasm-component-model` | WASM component model (calculator, sync) |
| `wasm-component-model-async` | WASM component model with async worker |
| `wasm-component-model-resource` | WASM component model with resources (RPN calc) |

---

## Contribution Points Used Across Samples

`commands`, `configuration`, `views`, `viewsContainers`, `viewsWelcome`, `walkthroughs`, `themes`, `productIconThemes`, `snippets`, `languages`, `grammars`, `colors`, `menus`, `taskDefinitions`, `customEditors`, `authentication`, `notebookRenderer`, `notebooks`, `chatParticipants`, `languageModelTools`, `languageModelChatProviders`, `chatContext`, `chatOutputRenderers`, `mcpServerDefinitionProviders`, `html.customData`, `css.customData`, `keybindings`, `terminal.profiles`, `browser` (web extension entry)

---

## Build/Run Instructions

**Standard TypeScript:**
1. `npm install`
2. `npm run compile` (or `npm run watch`)
3. F5 to launch Extension Development Host

**Webpack:** `npm run webpack` or `npm run vscode:prepublish`

**esbuild:** `node esbuild.js`

**LSP samples:** Multi-project (client/ + server/), `npm install` at root, `npm run compile`, F5

**Proposed API samples:** Need `@vscode/dts` (`npm run download-api`), VS Code Insiders only

**Web extensions:** `browser` field in package.json instead of `main`, test with `@vscode/test-web`

---

## API-to-Sample Reverse Lookup

| API/Feature | Sample(s) |
|-------------|-----------|
| Commands | helloworld-sample, helloworld-minimal, helloworld-test-*, document-editing, vim, many more |
| Webview | webview-sample |
| Webview View (sidebar) | webview-view-sample |
| Tree View | tree-view-sample |
| Status Bar | statusbar-sample, vim-sample |
| Progress | progress-sample |
| QuickPick/InputBox | quickinput-sample |
| Notifications | notifications-sample |
| CompletionItemProvider | completions-sample |
| CodeActionsProvider | code-actions-sample |
| CodeLensProvider | codelens-sample |
| CallHierarchyProvider | call-hierarchy-sample |
| SemanticTokensProvider | semantic-tokens-sample |
| TextDocumentContentProvider | contentprovider-sample, virtual-document-sample |
| FileSystemProvider | fsprovider-sample, nodefs-provider-sample |
| workspace.fs | fsconsumer-sample |
| Custom Editor | custom-editor-sample |
| Notebook | notebook-serializer-sample, notebook-renderer-sample, notebook-renderer-react-sample |
| Test Provider | test-provider-sample |
| Task Provider | task-provider-sample |
| SCM Provider | source-control-sample |
| Comments | comment-sample |
| Authentication | authenticationprovider-sample, github-authentication-sample |
| Terminal | terminal-sample, extension-terminal-sample, shell-integration-sample |
| Chat Participant | chat-sample, chat-tutorial |
| LM API | lm-api-tutorial, chat-sample |
| LM Tool | chat-sample |
| MCP | mcp-extension-sample |
| Chat Model Provider | chat-model-provider-sample |
| Chat Context Provider | chat-context-sample |
| Chat Output Renderer | chat-output-renderer-sample |
| LSP | lsp-sample, lsp-log-streaming, lsp-multi-server, lsp-web, lsp-user-input, lsp-embedded-* |
| WASM | wasm-component-model, wasm-component-model-async, wasm-component-model-resource, wasm-language-server |
| Tabs API | tabs-api-sample |
| Localization | l10n-sample |
| Decorations | decorator-sample |
| Walkthroughs | getting-started-sample |
| URI Handler | uri-handler-sample |
| Telemetry | telemetry-sample |