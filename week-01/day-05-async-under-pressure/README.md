# Day 5

Make it work under pressure.

## Goal

Build a small async FastAPI flow that calls public APIs without blocking the service.

## Time Box

1.5 to 2 hours

## Scenario

The user asks for a pack of 5 random dogs.

Your service must:

- fetch 5 random dog images
- detect the breed for each one
- if any dog is a German Shepherd, trigger a background task

The background task can:

- send a fake email
- or write a log entry

The user should get the API response without waiting for that side effect.

## What Students Must Build

1. one endpoint such as `GET /dogs/random-pack`
2. one async service that calls the public APIs
3. one background task for email or logging
4. tests for one happy path and one breed-triggered side effect

## Public APIs To Use

- `Dog CEO`: get a random dog image

Students should call both from the service layer, not from the endpoint.

## Suggested Structure

- endpoint: handles the HTTP request and response
- service: makes the API calls and decides whether to trigger the side effect
- background task: sends email or writes a log

## Required Behavior

When `GET /dogs/random-pack` is called:

- the endpoint calls the async service
- the service fetches 5 random dog images
- those 5 HTTP calls happen concurrently with `asyncio.gather(...)`
- the service decides the breed from each image URL
- if at least one breed is `germanshepherd`, a background task is triggered
- the endpoint returns the 5 image URLs and breeds

## Acceptance Criteria

- at least one endpoint is `async`
- the public API calls happen in the service layer
- the service performs 5 real HTTP requests concurrently
- a background task handles the side effect
- the response returns quickly
- tests cover one normal pack and one German Shepherd case

## Testing Focus

- mock the 5 Dog CEO responses
- assert the endpoint payload
- assert the side effect is triggered only for the target breed

## Deliverables

- one branch
- one PR named `day-5-<student-name>`
- one async endpoint
- one async service
- one background task
- updated tests
- a short PR note explaining:
  - where the API calls live
  - how they made the 5 calls concurrent
  - what moved to a background task
  - why the endpoint should not own external API logic

## API Reference

- Dog CEO docs: [dog.ceo/dog-api/documentation](https://dog.ceo/dog-api/documentation/)
