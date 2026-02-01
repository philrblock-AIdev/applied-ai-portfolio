# Student Services Intake Workflow (Human-in-the-Loop)

This document describes how AI-assisted intake classification and retrieval fit into a real student services workflow.

The AI system supports staff. It does not make final decisions.

---

## Step 1 — Student Inquiry Submitted
- Student submits a free-text inquiry via a portal or email
- Message is logged in the intake system

---

## Step 2 — AI Intake Classification
- The intake prompt classifies the inquiry category
- Confidence level is assessed conservatively
- Escalation requirement is flagged

Output includes:
- Category
- Confidence level
- Human review requirement
- Staff-facing summary

---

## Step 3 — Retrieval of Relevant Policy Documents
- If needed, the RAG system retrieves relevant institutional documents
- Retrieved sources are attached for staff visibility
- No documents are hidden from reviewers

---

## Step 4 — Human Review and Validation
- Staff review AI classification and retrieved context
- Staff may:
  - Approve the classification
  - Correct the category
  - Ignore AI output entirely

AI outputs never bypass human judgment.

---

## Step 5 — Staff Response or Escalation
- Staff respond to the student or route the case internally
- Sensitive or ambiguous cases are escalated according to policy

---

## Key Safeguards
- Conservative defaults
- Mandatory escalation for uncertainty
- Full transparency of AI inputs and sources
- Human override at every stage

---

## Why This Workflow Works
- Reduces response time
- Preserves institutional accountability
- Aligns with higher-education governance standards
- Minimizes operational risk
