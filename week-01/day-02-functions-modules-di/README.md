# Day 2

Write code that survives change.

## Goal

Take your Day 1 solution and make it easier to extend, test, and understand.

## Time Box

3 hours

## Core Ideas

- functions first, classes later
- composition over monolith functions
- clear module boundaries
- OOP only when it helps
- pass dependencies in, do not create them inside

## What Students Should Understand

- how to structure code beyond a single file
- when to use functions vs classes
- how to decouple code without overengineering

## Starting Point

Use your Day 1 refactor as the base.

If a team is behind, they can start from `week-01/day-01-project-setup-ai/starter_legacy_app/` and refactor from there.

## Students Must Do

1. Create a branch: `day-02/functions-and-design`
2. Break large logic into small functions
3. Split responsibilities into modules
4. Introduce one swappable behavior with a strategy
5. Inject at least one dependency instead of creating it internally
6. Add one small factory to centralize creation
7. Keep `ruff`, `ty`, and CI passing
8. Open one PR for Day 2

## What They Should Refactor

The main problems to attack are:

- large functions doing many jobs
- logic and I/O mixed together
- files that are hard to name
- conditionals that should become swappable behavior
- hard-coded dependencies created inside functions

## Suggested Module Shape

Students can choose the final structure, but a good direction is:

```text
src/
  processing/
  validators/
  services/
  repositories/
  cli/
```

They do not need to copy this exactly.
The point is clear boundaries, not perfect folder names.

## Practical Refactor Tasks

### Task 1: Break Into Functions

Turn large blocks into smaller functions such as:

- `validate_rows`
- `calculate_utilization`
- `group_by_client`
- `render_report`

Rule:

- one function, one clear job

### Task 2: Create Modules

Move code so responsibilities are separated.

Do not mix:

- business logic
- formatting
- file loading
- configuration

### Task 3: Add One Strategy

Use a strategy for one behavior that may vary.

Good examples:

- output format: text vs json
- scoring policy: normal vs aggressive
- input parsing: csv vs json

The goal is to replace a growing conditional with interchangeable behavior.

### Task 4: Add Dependency Injection

Before:

```python
def run():
    loader = FileLoader()
```

After:

```python
def run(loader):
```

Rule:

- do not create important dependencies inside the function that uses them

### Task 5: Add A Tiny Factory

Examples:

- `get_parser(file_type)`
- `get_scoring_strategy(mode)`
- `get_renderer(output_type)`

Keep it small.
The factory should reduce scattered object creation, not add complexity.

## Expected End State

- smaller functions
- cleaner module boundaries
- a `src/` package that is easier to read
- at least one protocol or interface-like abstraction if useful
- at least one injected dependency
- at least one simple strategy
- at least one small factory
- no unnecessary classes
- `ruff check` passing
- `ruff format --check` passing
- `ty check` passing
- CI still passing

## AI Prompts Students Can Use

- `Refactor this into smaller functions with clearer names`
- `Suggest a better module structure for this code`
- `Convert this conditional into a strategy pattern`
- `Explain whether a class is actually needed here`
- `Show how to inject this dependency instead of creating it inline`

## Deliverables

- one branch
- one PR named `day-2-<student-name>`
- one short PR note explaining:
  - what they split into functions
  - what modules they created
  - where they used a strategy
  - where they used dependency injection
  - one place where they avoided overengineering

## Review Focus

Look for:

- good naming
- clear boundaries
- simpler flow
- easy-to-swap behavior
- unnecessary classes or patterns

## Teaching Lines

- `Code is read more than it is written`
- `If it's hard to change, it's poorly designed`
- `Functions first, classes later`
- `Composition gives you options`

## Stretch

- add a second strategy implementation
- add a protocol for a renderer or loader
- split tests into smaller focused files
- remove one class that does not need to exist
