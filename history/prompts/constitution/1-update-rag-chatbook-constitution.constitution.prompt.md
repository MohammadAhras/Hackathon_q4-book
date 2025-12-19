---
id: 1
title: "Update RAG Chatbook Constitution"
stage: constitution
date_iso: "2025-12-19"
surface: "agent"
model: "Claude Code"
feature: "none"
branch: "main"
user: "user"
command: "/sp.constitution"
labels: ["constitution", "spec", "ai-book", "rag"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
prompt_text: |
  Project: AI-Spec–Driven Technical Book with Embedded RAG Chatbot

  Purpose:
  Author and deploy a technical book using Spec-Kit Plus and Claude Code with Docusaurus on GitHub Pages, including a tightly grounded RAG chatbot that answers questions strictly from the book content or user-selected text.

  Core principles:
  - Specification-first execution
  - Technical accuracy and verifiability
  - Developer-focused clarity
  - Reproducibility
  - Zero-hallucination AI behavior

  Book standards:
  - Format: Docusaurus (MD/MDX)
  - Deployment: GitHub Pages
  - Audience: Intermediate–advanced developers
  - Structure: Architecture, tooling, authoring workflow, RAG design, backend, frontend embed, testing
  - Readability: Flesch-Kincaid grade 10–12
  - All examples executable or deployable

  RAG standards:
  - Retrieval strictly from indexed book content
  - User-selected text overrides global retrieval
  - Mandatory source section citation
  - Deterministic, grounded responses

  Technical constraints:
  - Backend: FastAPI
  - Database: Neon Serverless Postgres
  - Vector DB: Qdrant Cloud (Free Tier)
  - AI: OpenAI Agents SDK / ChatKit SDK
  - Embeddings, chunking, schemas fully documented

  Quality validation:
  - No broken builds, links, or code
  - Hallucination and retrieval accuracy tests
  - Deployed chatbot works on GitHub Pages

  Decisions to document:
  - Chunking strategy
  - Embedding model
  - RAG architecture
  - Prompt design
  - Security boundaries

  Success criteria:
  - Successful book deployment
  - Reproducible setup
  - RAG chatbot answers only from source content
  - Selection-scoped answers enforced
  - All validation tests pass
response_text: |
  Successfully updated the project constitution at `.specify/memory/constitution.md` with specific details for the AI-Spec-Driven Technical Book with Embedded RAG Chatbot project. The updated constitution includes:
  
  - Five core principles: Specification-First Execution, Technical Accuracy and Verifiability, Developer-Focused Clarity, Reproducibility, and Zero-Hallucination AI Behavior
  - Book Standards section defining format, structure, and audience requirements
  - RAG Standards specifying content retrieval requirements
  - Technical Constraints outlining the technology stack
  - Quality Validation and Success Criteria sections
  - Governance section with version information
  
  Version was updated from 1.0.0 to 1.1.0 as new principles and sections were added. The changes follow semantic versioning rules.
outcome: |
  The constitution has been successfully updated with all project-specific details. The file is properly formatted with no remaining placeholder tokens. The sync impact report has been included at the top of the file.
evaluation: |
  The updated constitution accurately reflects the requirements and principles specified by the user. All sections are complete and properly formatted. The version number correctly follows semantic versioning rules.
---

## Summary of Changes

I've updated the project constitution to reflect the specific requirements for the AI-Spec-Driven Technical Book with Embedded RAG Chatbot project with the following changes:

1. Updated project name to "AI-Spec-Driven Technical Book with Embedded RAG Chatbot"
2. Added five core principles based on your specifications:
   - Specification-First Execution
   - Technical Accuracy and Verifiability
   - Developer-Focused Clarity
   - Reproducibility
   - Zero-Hallucination AI Behavior
3. Added dedicated sections for:
   - Book Standards
   - RAG Standards
   - Technical Constraints
   - Quality Validation
   - Success Criteria
4. Version updated to 1.1.0 to reflect addition of new principles and sections

The changes are now in effect in `.specify/memory/constitution.md`.

## Recommended Commit Message
`docs: amend constitution to v1.1.0 (RAG chatbook principles and standards)`