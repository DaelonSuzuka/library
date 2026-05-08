# OpenCode Configuration

Global config at `~/.config/opencode/`. Applied to all projects on this machine.

## Files

| File | Purpose |
|------|---------|
| `opencode.jsonc` | Main config: providers, agents, permissions, plugins |
| `SystemPrompt.txt` | System prompt for build and plan agents (Lode Coding method) |
| `VisionPrompt.txt` | Prompt for vision extraction agents |
| `package.json` | Plugin dependencies (opencode-gemini-auth for Gemini API access) |

## Providers

| Provider | Model ID | Name | Modality |
|----------|----------|------|-----------|
| ollama-cloud | gemini-3-flash-preview | Gemini 3 Flash | text+image → text |
| ollama-cloud | gemma4:31b | Gemma 4 31B | text+image → text |

Plugin: `opencode-gemini-auth@latest` — handles Gemini API key authentication.

## Agents

### build (primary agent)
- Mode: `primary`
- Prompt: `{file:./SystemPrompt.txt}` (Lode Coding method)
- Permissions: edit=allow, bash=allow (full write access)

### plan (read-only agent)
- Mode: `primary`
- Prompt: `{file:./SystemPrompt.txt}` (same Lode Coding prompt)
- Permissions: edit=deny, bash=deny (read-only planning mode)

### vision (subagent)
- Mode: `subagent`
- Model: `ollama-cloud/gemini-3-flash-preview`
- Prompt: `{file:./VisionPrompt.txt}`
- Description: "Read images and extract structured content for lode files"
- Color: `#2ecc71` (green)
- Steps: 50
- Permissions: read=allow, bash=allow, glob=allow, grep=allow, edit=allow, question=deny, todowrite=deny

### vision-gemma4 (fallback vision agent)
- Mode: `subagent`
- Model: `ollama-cloud/gemma4:31b`
- Prompt: `{file:./VisionPrompt.txt}`
- Description: "Fallback vision agent using Gemma 4"
- Color: `#f39c12` (orange)
- Steps: 50
- Permissions: same as vision agent

## Permissions (global)

```json
"external_directory": {
    "~/.config/opencode/**": "allow",
    "~/projects/**": "allow"
}
```

Both the opencode config directory and the projects directory are allowlisted for external directory access.

## Replicating on Another Machine

1. Copy `opencode.jsonc`, `SystemPrompt.txt`, `VisionPrompt.txt` to `~/.config/opencode/`
2. Run `npm install` or `bun install` in `~/.config/opencode/` to get the gemini-auth plugin
3. Set up Gemini API credentials (the plugin handles auth flow)
4. Ensure Ollama is running with the `ollama-cloud` provider configured for cloud model access

## Design Decisions

- **build vs plan**: Both use the same Lode Coding prompt, but plan agent is locked to read-only. Use plan mode for exploration and architecture decisions, build mode for implementation.
- **vision as subagent**: Vision agents can't ask questions or write todos — they extract content and write it to files. The main agent decides when to invoke vision.
- **Gemini as primary vision**: Proven most accurate for technical document reading across tested models (Gemini > Claude > GPT-4 for datasheet extraction).
- **Gemma 4 as fallback**: Useful for comparison when Gemini results are uncertain.