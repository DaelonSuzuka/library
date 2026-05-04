# Procedures

## Re-cloning All Repos

Run the `reclone.sh` script from `~/projects/library/`:

```bash
cd ~/projects/library
bash reclone.sh
```

This reads `lode/registry.md` and clones each repo into `repos/`. If a repo directory already exists, it skips it. After re-cloning, update all version markers in `lode/version-markers.md`.

## Staleness Check

For each repo in the registry:

1. `cd repos/<repo>` and run `git fetch`
2. Compare local HEAD against upstream HEAD
3. If behind, flag as stale in `version-markers.md`
4. Report which repos need updating

## Pulling Updates

For a specific repo:

1. `cd repos/<repo>` and run `git pull`
2. Inspect the commit history of what was pulled: `git log HEAD@{1}..HEAD`
3. Review the changes: `git diff HEAD@{1}..HEAD --stat` then `git diff HEAD@{1}..HEAD` for details
4. Identify which lode sections reference this repo
5. Review each affected lode section for accuracy — update if the changes invalidated something
6. Update the version marker in `lode/version-markers.md` with new date and commit hash

## Adding a New Repo

1. Clone the repo into `repos/`
2. Add an entry to `lode/registry.md` with the source URL
3. Create a version marker entry in `lode/version-markers.md`
4. If the repo relates to existing lode sections, update them
5. Commit the lode changes