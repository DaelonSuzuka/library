# Use Cases

## Directed Indexing

Point the librarian at a source and a topic. It reads the source deeply, extracts everything relevant, and produces a structured report.

Examples:
- "Find every API endpoint and data type in this SDK related to authentication"
- "Extract all configuration options and their defaults from this tool's source"
- "Map out the state machine transitions in this protocol implementation"

Output: a compiled report, not search results. Structured, complete, actionable.

## Synthesis

Point the librarian at multiple sources and ask it to figure out how they relate. It studies each source, identifies the interactions and contracts between them, and produces a unified picture.

Examples:
- "Study the frontend and backend repos for this service and compile everything I'd need to implement a new client from scratch"
- "Compare how these two SDKs implement the same protocol and document the differences"
- "Trace how data flows from this library through this middleware to this storage layer"

Output: a cross-repo understanding that no single repo's docs would provide. The kind of thing you'd normally spend hours figuring out by reading code in multiple tabs.

## Hands-Off Testing

The library exploits effort asymmetry: the librarian does expensive indexing upfront so consumers (coding subagents) can navigate the lode efficiently — binary search levels of improvement over grinding through raw source files.

Testing exploits the same asymmetry in the other direction: **you can afford to be expensive when creating tests.** You read the raw source freely, burn context formulating deep, complicated questions, then dispatch a consumer subagent with the librarian prompt and your question. If the consumer answers correctly with few tool calls, the lode is healthy. If it falls back to raw source files, the lode has gaps.

Loop: read source → craft question → dispatch subagent → check answer quality + tool call count → if bad, patch lode → retest.