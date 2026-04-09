# ML Training Program

This repository contains the hands-on labs for the ML Accelerator Program, published one day at a time.

The current version includes only Day 1 so the cohort can focus on the engineering cockpit before moving into the next topic.

## Current Structure

```text
week-01/
  day-01-project-setup-ai/
```

## Day 1 Covers

- terminal-first workflow
- Git basics and rebase-first setup
- `uv` and a proper `pyproject.toml`
- `ruff` and `ty` in the terminal
- GitHub Actions quality checks
- safe AI-assisted development practices

## Recommended Student Workflow

1. Fork this repository.
2. Clone the fork locally.
3. Add the original repository as `upstream`.
4. Create a dedicated branch for the day.
5. Open a pull request before the session ends.

## Git Baseline

Students should run this once on their machine:

```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
git config --global fetch.prune true
```

## Delivery Model

- one branch per day
- one pull request per day
- one short demo at the end of the session
- one PR note explaining what was built, how it was validated, and how AI was reviewed
