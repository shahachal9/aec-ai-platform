# AEC AI Platform

AI-powered quality and project intelligence platform for the AEC industry.

## Product vision

The platform starts with a **BIM QA Agent** and expands into specialized AEC agents:

1. **BIM QA Agent** — checks Revit/BIM models against configurable project/company standards.
2. **RFI Agent** — analyzes, summarizes and prioritizes RFIs.
3. **Submittal Agent** — monitors submittals and highlights overdue/high-priority items.
4. **Project QA/Risk Agent** — combines project signals into an evidence-backed project health view.

## Phase 1

The current branch establishes the development foundation:

- FastAPI backend
- PostgreSQL + SQLAlchemy foundation
- Redis infrastructure
- Docker Compose
- Pydantic configuration/schemas
- Health/readiness APIs
- Initial organization API
- Pytest tests
- Frontend application shell
- Architecture documentation

Autodesk APS integration and AI agent functionality are intentionally deferred to later phases.

## Local development

### Docker

```bash
docker compose up --build
```

Open:

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Swagger: http://localhost:8000/docs
- Health: http://localhost:8000/health
- Readiness: http://localhost:8000/ready

### Backend tests

```bash
cd backend
pip install -r requirements.txt
pytest
```

## Architecture principle

Deterministic BIM validation is performed by a rules engine. The AI agent will interpret user intent, call controlled tools, explain evidence and eventually request confirmation for external write actions. The LLM is not the source of truth for QA pass/fail decisions.
