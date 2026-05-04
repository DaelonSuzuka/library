# Terminology

- **Registry** — tracked list of all external repos with source URLs
- **Version marker** — date + commit hash pinned to a cloned repo
- **Staleness check** — comparing local version markers against upstream HEAD
- **Directed indexing** — querying a single source for capabilities around a specific topic (e.g., "find every API endpoint and data type related to auth")
- **Synthesis** — querying multiple sources to understand how they relate and produce a unified report (e.g., "study how frontend and backend interact, compile what's needed for a new client")
- **Re-clone** — wiping `repos/` and re-cloning everything from the registry