# Practices

## Version Markers

- Every cloned repo must have a version marker (date + commit hash)
- Markers must be updated after every pull
- Never skip the verify step after pulling — always check if lode sections need updating

## Registry

- Every repo in `repos/` must have a corresponding entry in `lode/registry.md`
- The registry is the source of truth for what the library contains

## Effort Asymmetry

- The librarian burns context upfront so consumers don't have to
- Library artifacts are for agents, not humans — prose quality doesn't matter, completeness and structure do
- This means testing is cheap: you can read raw source to craft deep questions, then measure whether a consumer subagent answers efficiently through the lode
- Metric: tool call count. Few calls = lode is doing its job. Falling back to raw source = lode has gaps

## Reports

- Directed indexing and synthesis queries produce structured reports, not raw search results
- Reports should be saved to `lode/tmp/` or a project-specific lode, not the library lode itself