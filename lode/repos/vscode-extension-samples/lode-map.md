# VS Code Extension Samples — Lode Map

```
lode/repos/vscode-extension-samples/
├── summary.md       # overview, sample categories, API reverse lookup
└── lode-map.md      # this file
```

This lode provides deep path references for all 81+ extension samples. The summary.md API-to-sample reverse lookup is the primary agent tool for finding samples by capability.

---

## Master Registry

The file `.scripts/samples.ts` defines two arrays:
- `samples[]` — 80 general extension API samples
- `lspSamples[]` — 10 LSP samples

Each entry has: `path`, `description`, `guide` (link to vscode-docs), `apis`, `contributions`, `excludeFromReadme`.

---

## Getting Started & Basic Samples

| Sample | Key Files | APIs | Guide |
|--------|-----------|------|-------|
| `helloworld-sample` | `src/extension.ts` | commands | — |
| `helloworld-minimal-sample` | `extension.js` | commands | — |
| `helloworld-test-sample` | `src/extension.ts`, `src/test/` | commands | — |
| `helloworld-test-cli-sample` | `src/extension.ts`, `src/test/` | commands | — |
| `helloworld-web-sample` | `src/web/extension.ts` | commands (web) | — |
| `getting-started-sample` | `src/extension.ts` | walkthroughs | — |
| `configuration-sample` | `src/extension.ts` | workspace.get | — |

## Bundling Samples

| Sample | Key Files | Bundler | Guide |
|--------|-----------|---------|-------|
| `webpack-sample` | `src/extension.ts`, `src/math.ts` | webpack | bundling-extension |
| `esbuild-sample` | `src/extension.ts`, `src/math.ts` | esbuild | bundling-extension |

## Language Features Samples

| Sample | Key Files | APIs | Guide |
|--------|-----------|------|-------|
| `completions-sample` | `src/extension.ts` | CompletionItemProvider | — |
| `code-actions-sample` | `src/extension.ts`, `src/diagnostics.ts` | CodeActionsProvider | — |
| `codelens-sample` | `src/CodelensProvider.ts`, `src/extension.ts` | CodeLensProvider | — |
| `semantic-tokens-sample` | `src/extension.ts` | DocumentSemanticTokensProvider | semantic-highlight-guide |
| `snippet-sample` | `snippets.json` | snippets | snippet-guide |
| `call-hierarchy-sample` | `src/FoodPyramidHierarchyProvider.ts` | CallHierarchyProvider | — |
| `inline-completions` | `src/extension.ts` | InlineCompletionItemProvider | — |
| `diagnostic-related-information-sample` | `src/extension.ts` | DiagnosticRelatedInformation | — |
| `document-paste` | `src/extension.ts` | DocumentPaste | — |

## LSP Samples

| Sample | Key Files | Guide |
|--------|-----------|-------|
| `lsp-sample` | `client/src/extension.ts`, `server/src/server.ts` | language-server-extension-guide |
| `lsp-log-streaming-sample` | `client/src/extension.ts`, `server/src/server.ts` | — |
| `lsp-multi-server-sample` | `client/src/extension.ts`, `server/src/server.ts` | — |
| `lsp-web-extension-sample` | `client/src/browserClientMain.ts`, `server/src/browserServerMain.ts` | language-server-extension-guide |
| `lsp-user-input-sample` | `client/`, `server/` | — |
| `lsp-embedded-language-service` | `client/`, `server/src/modes/` | — |
| `lsp-embedded-request-forwarding` | `client/`, `server/` | — |
| `wasm-language-server` | `client/`, `server/src/main.rs` | — |
| `language-configuration-sample` | `language-configuration.json` | language-configuration-guide |

## Editor Feature Samples

| Sample | Key Files | APIs |
|--------|-----------|------|
| `document-editing-sample` | `src/extension.ts` | WorkspaceEdit |
| `decorator-sample` | `src/extension.ts` | TextEditor.setDecorations, DecorationOptions |
| `contentprovider-sample` | `src/provider.ts`, `src/referencesDocument.ts` | TextDocumentContentProvider |
| `virtual-document-sample` | `src/extension.ts` | TextDocumentContentProvider |

## UI & View Samples

| Sample | Key Files | APIs | Guide |
|--------|-----------|------|-------|
| `webview-sample` | `src/extension.ts`, `media/` | window.createWebviewPanel | webview |
| `webview-view-sample` | `src/extension.ts`, `media/` | window.registerWebviewViewProvider | — |
| `webview-codicons-sample` | `src/extension.ts` | Webview + Codicons | — |
| `tree-view-sample` | `src/` (7 providers) | TreeDataProvider, TreeView | tree-view |
| `statusbar-sample` | `src/extension.ts` | window.createStatusBarItem | — |
| `progress-sample` | `src/extension.ts` | window.withProgress | — |
| `quickinput-sample` | `src/basicInput.ts`, `src/multiStepInput.ts` | QuickInput | — |
| `notifications-sample` | `src/extension.ts` | window.showInformationMessage, etc. | — |

## Chat & AI Samples

| Sample | Key Files | APIs |
|--------|-----------|------|
| `chat-sample` | `src/extension.ts`, `src/simple.ts`, `src/tools.ts`, `src/play.tsx`, `src/toolParticipant.ts` | ChatParticipant, LanguageModelChat |
| `chat-tutorial` | `src/extension.ts` | ChatParticipant |
| `chat-model-provider-sample` | `src/extension.ts`, `src/provider.ts` | LanguageModelChatProvider |
| `lm-api-tutorial` | `src/extension.ts` | LanguageModelChat |
| `mcp-extension-sample` | `src/extension.ts` | MCP |
| `chat-context-sample` | `src/extension.ts` | chatContextProvider |
| `chat-output-renderer-sample` | `src/extension.ts` | ChatOutputRenderer |

## Notebook Samples

| Sample | Key Files | Guide |
|--------|-----------|-------|
| `notebook-serializer-sample` | `src/extension.ts`, `src/serializer.ts`, `src/controller.ts` | notebook |
| `notebook-renderer-sample` | `src/index.ts`, `src/render.ts` | notebook-renderer |
| `notebook-renderer-react-sample` | `src/client/` | notebook-renderer |
| `notebook-extend-markdown-renderer-sample` | `src/emoji.ts` | notebook-renderer |
| `notebook-format-code-action-sample` | `src/extension.ts` | — |
| `jupyter-server-provider-sample` | `src/extension.ts`, `src/jupyter.ts` | — |
| `jupyter-kernel-execution-sample` | `src/extension.ts` | — |

## Terminal Samples

| Sample | Key Files | APIs |
|--------|-----------|------|
| `terminal-sample` | `src/extension.ts` | window.createTerminal, onDidOpenTerminal, etc. |
| `extension-terminal-sample` | `src/extension.ts` | window.Pseudoterminal |
| `shell-integration-sample` | `src/extension.ts` | ShellIntegration |

## File System Samples

| Sample | Key Files | APIs |
|--------|-----------|------|
| `fsprovider-sample` | `src/extension.ts`, `src/fileSystemProvider.ts` | workspace.registerFileSystemProvider |
| `fsconsumer-sample` | `src/extension.ts` | workspace.fs |
| `nodefs-provider-sample` | `src/extension.ts` | workspace.registerFileSystemProvider (node) |

## Theme & Icon Samples

| Sample | Key Files | Guide |
|--------|-----------|-------|
| `theme-sample` | `Sample_Dark.tmTheme`, `Sample_Light.tmTheme` | color-theme |
| `product-icon-theme-sample` | `icons/`, `theme/v1-product-icon-theme.json`, `build/updateFont.js` | product-icon-theme |
| `custom-data-sample` | `css.css-data.json`, `html.html-data.json` | custom-data-extension |

## Other Samples

| Sample | Key Files | APIs |
|--------|-----------|------|
| `task-provider-sample` | `src/customTaskProvider.ts`, `src/rakeTaskProvider.ts` | tasks.registerTaskProvider |
| `source-control-sample` | `src/afs.ts`, `src/fiddleSourceControl.ts` | scm.createSourceControl |
| `comment-sample` | `src/extension.ts` | Commenting API |
| `custom-editor-sample` | `src/catScratchEditor.ts`, `src/pawDrawEditor.ts` | window.registerCustomEditorProvider |
| `test-provider-sample` | `src/extension.ts`, `src/testTree.ts`, `src/parser.ts` | TestProvider |
| `vim-sample` | `src/controller.ts`, `src/motions.ts`, `src/operators.ts` | Commands, StatusBarItem |
| `authenticationprovider-sample` | `src/authProvider.ts` | AuthenticationProvider |
| `github-authentication-sample` | `src/credentials.ts` | Authentication |
| `l10n-sample` | `src/extension.ts`, `l10n/bundle.l10n.ja.json` | l10n |
| `uri-handler-sample` | `src/extension.ts` | UriHandler |
| `proposed-api-sample` | `src/extension.ts` | Proposed API |
| `tabs-api-sample` | `src/extension.ts` | Tab Groups |
| `telemetry-sample` | `src/extension.ts` | Telemetry |
| `welcome-view-content-sample` | `src/extension.ts` | Walkthrough |
| `drop-on-document` | `src/extension.ts` | DocumentDropEdit |

## WASM Samples

| Sample | Key Files | Runtime |
|--------|-----------|---------|
| `wasm-component-model` | `src/calculator.ts`, `src/lib.rs`, `wit/calculator.wit` | WASI Component Model |
| `wasm-component-model-async` | `src/calculator.ts`, `src/lib.rs`, `src/worker.ts` | WASI Component Model (async) |
| `wasm-component-model-resource` | `src/calculator.ts`, `src/calculator.rs`, `wit/calculator.wit` | WASI Component Model (resource) |
| `wasm-language-server` | `client/`, `server/src/main.rs`, `testbed/` | WASM Language Server |

---

## Base Template

`.base-sample/` — Canonical scaffold with `package.json`, `tsconfig.json`, `eslint.config.mjs`, `.vscode/` configs, and `src/extension.ts`. New samples should mirror this structure.

---

## Build/Run

Standard: `npm install && npm run compile`, F5 to launch.
LSP samples: Multi-project (`client/` + `server/`), `npm install` at root.
Web extensions: `browser` field in package.json, test with `@vscode/test-web`.