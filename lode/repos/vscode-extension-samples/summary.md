# VS Code Extension Samples

**Repository Root:** `repos/vscode-extension-samples`
**Organization:** Each sample is a standalone extension (81 samples total)
**API Target:** `^1.100.0` (most samples)
**Build:** TypeScript (`tsc`), some use webpack or esbuild

## Key Files

| File | Purpose |
|------|---------|
| `.base-sample/` | Canonical scaffold (package.json, tsconfig, eslint, .vscode/) |
| `.scripts/samples.ts` | Master registry: `samples[]`, `lspSamples[]` with description, APIs, contributions |

## Sample Categories

| Category | Count | Key Samples |
|----------|-------|-------------|
| Getting Started | 5 | helloworld, helloworld-minimal, helloworld-test-*, helloworld-web |
| Bundling | 2 | webpack-sample, esbuild-sample |
| Language Features | 9 | completions, code-actions, codelens, semantic-tokens, snippets |
| LSP | 8 | lsp-sample, lsp-log-streaming, lsp-multi-server, lsp-web, wasm-language-server |
| Editor Features | 6 | document-editing, decorator, contentprovider, virtual-document |
| UI & Views | 10 | webview, tree-view, statusbar, progress, quickinput, notifications |
| Chat & AI | 7 | chat-sample, chat-tutorial, chat-model-provider, mcp-extension-sample, lm-api-tutorial |
| Notebooks | 7 | notebook-serializer, notebook-renderer, notebook-renderer-react, jupyter-* |
| Terminal | 3 | terminal-sample, extension-terminal, shell-integration |
| File System | 3 | fsprovider, fsconsumer, nodefs-provider |
| Themes & Icons | 3 | theme-sample, product-icon-theme-sample, custom-data-sample |
| WASM | 4 | wasm-component-model, wasm-component-model-async, wasm-component-model-resource, wasm-language-server |
| Other | 14 | test-provider, task-provider, source-control, comment, custom-editor, vim, proposed-api, etc. |

## API-to-Sample Reverse Lookup

| API/Feature | Sample(s) |
|-------------|-----------|
| Webview | webview-sample |
| Tree View | tree-view-sample |
| CompletionItemProvider | completions-sample |
| CodeActionsProvider | code-actions-sample |
| CodeLensProvider | codelens-sample |
| SemanticTokensProvider | semantic-tokens-sample |
| FileSystemProvider | fsprovider-sample, nodefs-provider-sample |
| Custom Editor | custom-editor-sample |
| Notebook | notebook-serializer-sample, notebook-renderer-* |
| Chat Participant | chat-sample, chat-tutorial |
| LM API / Tool | lm-api-tutorial, chat-sample |
| MCP | mcp-extension-sample |
| LSP | lsp-sample, lsp-log-streaming, lsp-multi-server, lsp-web, lsp-embedded-* |

## Build/Run

Standard TS: `npm install && npm run compile`, F5 to launch
LSP: Multi-project (client/ + server/), `npm install` at root
Web extensions: `browser` field in package.json, test with `@vscode/test-web`

## Deep Index

See [lode-map.md](lode-map.md) for a complete file-level path index of every sample, its key source files, APIs, and guide links.

## See Also

- [lode-map.md](lode-map.md)
