# What to Try Next in This Repository

This repository currently contains only a `.gitkeep` file and no project code yet.

## 1) Pick a stack and create a runnable skeleton (Day 0)
Choose one:
- **Python API**: FastAPI + Uvicorn + pytest + ruff
- **Node API**: TypeScript + Express/Fastify + vitest + eslint
- **CLI tool**: Python `typer` or Node `commander`

Goal: you should be able to run one command and see a healthy startup.

## 2) Add baseline repository files (first commit after scaffold)
Create these files early:
- `README.md` (setup, run, test, architecture notes)
- `.gitignore`
- `LICENSE`
- `.editorconfig`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CODEOWNERS` (if team repo)

## 3) Wire quality gates in CI (must-have)
Set up a GitHub Actions workflow to run on pull requests:
- format/lint
- unit tests
- dependency audit / SCA
- secret scanning

Block merge unless checks pass.

## 4) Security-first defaults (before feature work)
- Never commit secrets; use environment variables and a `.env.example` template.
- Enable branch protection (`main` protected, PR required, status checks required).
- Enable Dependabot updates + alerts.
- Add pre-commit hooks (`detect-secrets` or `gitleaks`, formatter, linter).

## 5) Build one thin vertical slice (Week 1)
Ship one end-to-end feature:
- input validation
- business logic
- tests
- logging
- error handling

Keep it small. The goal is a deployable pattern you can copy.

## 6) Add observability from day one
- structured logs (JSON preferred)
- request IDs/correlation IDs
- basic health check endpoint (`/healthz`)
- failure alerts for CI and runtime

## 7) Decide your delivery model now
- local run (`make run` / `npm run dev` / `uv run`)
- containerized run (`Dockerfile`)
- environment promotion strategy (dev -> staging -> prod)

## Suggested immediate next 3 tasks for *this* repo
1. Add a `README.md` with quickstart and repo purpose.
2. Add a minimal GitHub Actions CI workflow.
3. Scaffold your first runnable service (API or CLI) with tests.

If you want, I can generate a full production-ready starter in one pass (for Python FastAPI or Node TypeScript) including CI, security scans, and local dev commands.
