# Roadmap

## Server-Hosted Library

Move the master copy of the library to the proxmox server. An agent harness (hermes) autonomously maintains it — staleness checks, pulling updates, verifying lode sections. Dependency: proxmox rack rebuild. Related: `~/projects/lode/roadmap.md`.

## Librarian Agent Release

Package the library structure, procedures, directed indexing, synthesis, and hands-off testing as a reusable "librarian agent" project. Preconfigured so others can deploy it and start indexing their own reference repos.