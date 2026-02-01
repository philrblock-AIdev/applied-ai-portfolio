# Applied AI Portfolio Demo Script

## Introduction (30 seconds)

“This portfolio demonstrates how I design and evaluate applied AI systems for higher-education student services.

The focus is not on model training, but on prompt engineering, guardrails, retrieval, evaluation, and human-in-the-loop workflows.”

---

## Problem Context (30 seconds)

“Student services teams receive large volumes of free-text inquiries.
The challenges are:
- Correctly routing requests
- Avoiding hallucinated answers
- Ensuring sensitive cases are escalated
- Keeping humans in control”

---

## Prompt Design (60 seconds)

“I designed structured prompt frameworks with:
- Explicit system roles
- Strict output formats
- Conservative escalation rules
- Versioned iteration (v1 → v2)

This ensures prompts behave predictably and can be audited.”

(Show `01_prompt_library`)

---

## Retrieval-Augmented Generation (60 seconds)

“I implemented a simple RAG pipeline that:
- Loads institutional policy documents
- Retrieves relevant sources based on the query
- Grounds the prompt in authoritative text
- Forbids policy invention”

(Show `rag_pipeline.py` output)

---

## Evaluation & Testing (45 seconds)

“I created an evaluation rubric and representative test cases to score outputs on:
- Accuracy
- Guardrail compliance
- Escalation correctness
- Output structure”

(Show `03_evaluation`)

---

## Human-in-the-Loop Workflow (45 seconds)

“The AI never makes final decisions.
Every step includes:
- Human visibility
- Override capability
- Conservative defaults for uncertainty”

(Show `04_workflows`)

---

## Closing (30 seconds)

“This approach reflects how applied AI systems are actually deployed in regulated environments:
Assistive, auditable, and human-centered.”

