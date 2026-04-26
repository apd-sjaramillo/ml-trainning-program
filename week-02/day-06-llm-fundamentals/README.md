# Day 6

Think like the model.

## Goal

Build one endpoint that uses a local Ollama model as a guardrail before sending safe questions to a stronger answer model.

## Time Box

1.5 to 2 hours

## Skills Slide

See [SLIDES.md](/Users/santiagojaramillo/Documents/ML Accelerator Program/ml-trainning-program/week-02/day-06-llm-fundamentals/SLIDES.md).

## Exercise

Inside `llm_guardrail_service/` there is a standalone FastAPI project for this day.

Students must build `POST /ask` using the endpoint -> service -> repository pattern.

### What Is Already Given

- a standalone `uv` project
- one working local Ollama client
- schemas for request, guardrail decision, and response
- one SQLite audit repository
- one mock answer service
- one health endpoint
- starter tests

### What Students Must Build

1. write a strong guardrail prompt for the local model
2. implement the guardrail classification flow
3. implement the orchestrator service
4. call the local Ollama guardrail service first
5. block harassment or prompt injection
6. call the answer service only for safe questions
7. persist the decision in the audit repository
8. implement `POST /ask`
9. write or unskip the tests and make them pass

## Acceptance Criteria

- local model is used first
- guardrail output is structured
- unsafe questions never reach the answer service
- safe questions do reach the answer service
- endpoint returns a consistent response schema
- audit rows are written to SQLite
- the prompt is explicit enough to make the guardrail output reliable

## Deliverables

- one branch
- one PR named `day-6-<student-name>`
- one working `POST /ask` endpoint
- passing tests
- a short PR note explaining:
  - why the local model comes first
  - what the structured guardrail output looks like
  - how they improved the prompt
  - where the answer model is called
  - what gets stored in the repository
