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