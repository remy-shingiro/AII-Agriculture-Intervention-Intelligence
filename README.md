# Agricultural Intervention Intelligence

## Project Purpose

Agricultural Intervention Intelligence is a production-oriented foundation for a future system that will use NISR Rwanda agricultural data to identify productivity gaps and prioritize potential interventions such as irrigation, improved seeds, soil and fertilizer management, agricultural extension, anti-erosion measures, and mechanisation.

## Current Architecture

The project follows Clean Architecture:

- `domain/`: business concepts and rules, independent of frameworks and infrastructure.
- `application/`: use cases and application orchestration.
- `infrastructure/`: data processing, machine learning, persistence, and configuration.
- `interfaces/`: API and command-line entry points.

The source package is under `src/agri_intelligence/`. Tests are organized under `tests/` by test scope.

## Planned Technology Stack

- Python 3.12
- uv
- pandas, NumPy, PyArrow
- Pydantic and pydantic-settings
- pytest, Ruff, mypy, and pre-commit

Future dependencies will be added only when implementation requires them.

## Development Setup

Install uv, then create the environment and install the project with development dependencies:

```bash
uv sync
uv run pre-commit install
```

## Quality Checks

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

## Data and Repository Rules

- Never commit raw NISR microdata, generated datasets, or model artifacts.
- Never commit secrets; use `.env` locally and `.env.example` for non-secret configuration names.
- Keep dependencies pointed inward: domain code must remain independent of frameworks and infrastructure.
- Do not use outcome variables as predictive features or make causal claims from predictive models.
- Review the Git diff before finishing changes.

## Current Scope

This repository contains project foundation and quality tooling only. The data ingestion and harmonization pipeline, productivity models, productivity target, intervention signals, priority scoring, API, and frontend are not implemented yet.
