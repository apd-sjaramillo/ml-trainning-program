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

## Repo Strategy

By default, the course should use one shared Python project at the repository root:

- one root `pyproject.toml`
- one root `uv.lock`
- one root `.venv`
- one root `.github/workflows/`

Day folders should usually contain:

- instructions
- starter files
- datasets
- day-specific notes

This helps students learn `uv` the way they will use it in a real repository.

### Default Rule

Reuse the same root project when the day builds on previous work.

### Exception Rule

Create a separate subproject with its own `pyproject.toml` only when the day is truly independent, such as:

- a standalone FastAPI app
- a separate RAG prototype
- a LangGraph app with very different dependencies
- a capstone project

## UV Learning Goal

Students should repeatedly practice:

- `uv init`
- `uv add`
- `uv add --dev`
- `uv sync`
- `uv run`
- `uv lock`
- `uv tree`

The goal is not one `pyproject.toml` per day.
The goal is understanding how to manage a real project well.

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
