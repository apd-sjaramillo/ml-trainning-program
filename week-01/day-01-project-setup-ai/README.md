# Day 1

Build order from chaos.

## Goal

Take the legacy code in `starter_legacy_app/` and turn it into a clean Python project.

## Time Box

3 hours

## Students Must Do

1. Fork the repo and clone from the terminal.
2. Add `upstream`.
3. Configure rebase as default:

```bash
git config pull.rebase true
git config rebase.autoStash true
```

4. Create a branch: `day-01/project-cockpit`
5. Restructure the legacy code into a proper project.
6. Create a real `pyproject.toml` with `uv`.
7. Apply `ruff` and `ty`.
8. Add GitHub Actions for `ruff` and `ty`.
9. Open a PR.

## Legacy App Rules

The code in `starter_legacy_app/` is intentionally bad:

- very long files
- weak naming
- mixed responsibilities
- no typing
- poor structure
- one long test

It should still run before students refactor it.

## What The Legacy App Does

The starter app generates a simple utilization report for a consulting team.

It has three pieces:

- `report_utils_everything.py`
  Loads hard-coded consultant data, calculates utilization and score, groups results, and builds the final report data.
- `report_runner.py`
  Runs the report and prints it to the terminal.
- `test_super_long_legacy_flow.py`
  Checks that the current behavior works end to end.

The data represents consultants working for different clients, departments, and countries.

For each consultant, the code calculates:

- hours worked
- available capacity
- utilization percentage
- a score
- a simple performance band like `excellent`, `strong`, `ok`, or `risk`

It also produces summary information such as:

- total people
- total hours
- billable vs non-billable hours
- utilization by client

Students do not need to change the business idea.
Their job is to keep the behavior but improve the engineering quality.

## What Students Should Refactor

A good Day 1 result would move from "one messy script" to "clean project structure".

Examples of improvements they can make:

- split loading, calculation, formatting, and CLI concerns
- create a package under `src/`
- add typing and docstrings
- make names clearer
- break large functions into smaller units
- replace the long test with better organized tests
- add `ruff`, `ty`, and CI

## Expected End State

- `src/` layout
- `pyproject.toml`
- `uv.lock`
- modules and folders decided by the student
- typed code
- `.github/workflows/ci.yml` or `.github/workflows/ci.yaml`
- `ruff check` passing
- `ruff format --check` passing
- `ty check` passing
- CI passing in GitHub Actions

## Deliverables

- one branch
- one PR named `santiago-day-1-<student-name>` or `day-1-<student-name>`
- one `docs/ai-usage.md`
- one short PR note explaining:
  - what they reorganized
  - what `ruff` found
  - what `ty` found
  - what AI suggested and what they rejected

## Naming Recommendation

To keep reviews easy, use one PR per day and one consistent naming rule.

Recommended PR title:

`day-1-<student-name>`

If you want all PRs grouped under your name in GitHub search, use:

`santiago-day-1-<student-name>`

The shorter option is usually better because it is easier to scan.

## Stretch

- add `.env.example`
- add a small CLI entrypoint
- add a second test after the refactor
