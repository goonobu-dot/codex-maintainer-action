# Beginner-Friendly Guide

This page explains Codex Maintainer Action in plain language.

## What this project is

Codex Maintainer Action is a GitHub Actions wrapper for Codex Maintainer Kit.

That means it runs the maintainer health check automatically inside GitHub.

It can create files such as:

- `OSS_MAINTENANCE_AUDIT.md`
- `MAINTAINER_BRIEF.md`
- `CODEX_TASKS.md`
- `codex-tasks.json`
- `CODEX_REVIEW.md`

These files help maintainers decide what needs attention.

## Why it exists

Running a maintenance check by hand is useful, but people forget.

GitHub Actions can run checks on a schedule or when someone starts them manually. This action makes the maintainer check repeatable inside GitHub.

## Simple analogy

Imagine a classroom inspection that runs every Monday.

It checks the room and creates a report. The report says what needs attention, but it does not move desks or throw anything away by itself.

Codex Maintainer Action works the same way for a GitHub project.

## What it does not do

- It does not auto-merge pull requests.
- It does not auto-release code.
- It does not give Codex write access.
- It does not replace a maintainer.

It creates reviewable maintenance artifacts. A human still decides what to do.

## When to use it

Use it when a GitHub repository should regularly create maintenance reports and task lists.

Use Codex Maintainer Kit directly when you want to run the same check locally on your own machine.
