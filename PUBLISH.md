# Publish Instructions

This package is already initialized as a local git repository on branch `main`.

## GitHub

Authenticate first if needed:

```bash
gh auth login
```

Create and push a public repo:

```bash
gh repo create cloud-agent-damage-audit --public --source=. --remote=origin --push
```

Create and push a private repo:

```bash
gh repo create cloud-agent-damage-audit --private --source=. --remote=origin --push
```

## Verify

```bash
git remote -v
git status --short
```

## Portfolio Use

After publishing, use the GitHub URL in:

- AI red-team contract applications
- partner outreach
- grant/credits proposals
- social posts
