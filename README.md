# ML Training Program

This repository contains the hands-on labs for the ML Accelerator Program, published one day at a time.

The current version includes Day 1 and Day 2.

## Current Structure

```text
week-01/
  day-01-project-setup-ai/
  day-02-functions-modules-di/
```

## Current Days

- Day 1: terminal-first workflow, Git basics, `uv`, `pyproject.toml`, `ruff`, `ty`, GitHub Actions, safe AI usage
- Day 2: functions, composition, module boundaries, pragmatic OOP, protocols, dependency injection, strategy and factory basics

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
