# Phase 0 Architecture Baseline

The platform is a modular monolith designed for a commercial multi-tenant AEC SaaS product.

## Core decisions

- FastAPI + Python backend
- PostgreSQL primary database
- Redis for background-job infrastructure
- Web frontend
- Autodesk Platform Services adapter layer
- AEC Data Model as the planned BIM data source for the MVP
- Deterministic BIM QA rules engine
- Tool-based AI agent above deterministic services
- Organization-based multi-tenancy
- RBAC and auditability
- Unit, integration, contract and agent tests

## Product agents

1. BIM QA Agent — MVP
2. RFI Agent — future
3. Submittal Agent — future
4. Project QA/Risk Agent — future

The LLM must not be the source of truth for deterministic QA pass/fail decisions.
