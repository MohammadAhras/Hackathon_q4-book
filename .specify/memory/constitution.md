<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles:
Added sections: Book Standards, RAG Standards, Technical Constraints, Quality Validation, Decisions to Document, Success Criteria
Removed sections: None
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# AI-Spec-Driven Technical Book with Embedded RAG Chatbot Constitution

## Core Principles

### I. Specification-First Execution
Specification-first execution: All features and implementations begin with comprehensive specifications; Code and deployment follow approved specs; Changes to functionality require spec updates first.

### II. Technical Accuracy and Verifiability
Technical accuracy and verifiability: All technical claims must be verifiable through testing or documentation; Code examples must be executable or deployable as described; Citations required for external sources.

### III. Developer-Focused Clarity
Developer-focused clarity: All content and interfaces designed for intermediate-advanced developers; Documentation must be practical and implementation-oriented; Clear error messages and debugging guidance required.

### IV. Reproducibility
Reproducibility: All setup, build, and deployment processes must be reproducible on different systems; Configuration must be well-documented and deterministic; Dependency management follows strict version controls.

### V. Zero-Hallucination AI Behavior
Zero-hallucination AI behavior: The RAG chatbot must only respond with information sourced from the book content or user-selected text; No generated content that isn't grounded in source material; Strict retrieval accuracy enforced.

## Book Standards

### Format and Structure
Format: Docusaurus (MD/MDX); Deployment: GitHub Pages; Audience: Intermediate–advanced developers; Structure: Architecture, tooling, authoring workflow, RAG design, backend, frontend embed, testing; Readability: Flesch-Kincaid grade 10–12; All examples executable or deployable.

## RAG Standards

### Content Retrieval
Retrieval strictly from indexed book content; User-selected text overrides global retrieval; Mandatory source section citation; Deterministic, grounded responses.

## Technical Constraints

### Technology Stack
Backend: FastAPI; Database: Neon Serverless Postgres; Vector DB: Qdrant Cloud (Free Tier); AI: OpenAI Agents SDK / ChatKit SDK; Embeddings, chunking, schemas fully documented.

## Quality Validation

### Validation Requirements
No broken builds, links, or code; Hallucination and retrieval accuracy tests; Deployed chatbot works on GitHub Pages; All examples in the book are tested and verified.

## Success Criteria

### Project Completion Metrics
Successful book deployment; Reproducible setup; RAG chatbot answers only from source content; Selection-scoped answers enforced; All validation tests pass.

## Governance

All implementations must comply with these principles; Amendments require documentation of rationale and impact assessment; Versioning follows semantic versioning based on principle changes; Compliance reviews conducted before each release.

**Version**: 1.1.0 | **Ratified**: 2025-06-13 | **Last Amended**: 2025-12-19
