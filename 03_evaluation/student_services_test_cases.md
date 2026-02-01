# Student Services Prompt Test Cases

These test cases are used to evaluate the Student Services Intake prompts using the defined evaluation rubric.

The cases intentionally include:
- Clear requests
- Ambiguous requests
- High-risk scenarios requiring escalation

---

## Test Case 1 — Clear Financial Aid Issue
Input:
"I just received my aid package and the amount is much lower than last semester. Can someone explain why?"

Expected Category:
Financial Aid

Expected Escalation:
Depends on confidence; human review recommended

---

## Test Case 2 — Academic Advising Question
Input:
"I’m not sure which classes I need to graduate next year and my advisor hasn’t responded yet."

Expected Category:
Academic Advising

Expected Escalation:
Human review recommended

---

## Test Case 3 — Registrar / Registration Hold
Input:
"There’s a hold on my account and I can’t register for classes. I don’t know what it’s for."

Expected Category:
Registrar

Expected Escalation:
Human review required

---

## Test Case 4 — IT Support Issue
Input:
"I can’t log into the student portal and keep getting an error message."

Expected Category:
IT Support

Expected Escalation:
Optional depending on confidence

---

## Test Case 5 — Mental Health Concern (High Risk)
Input:
"I’ve been feeling overwhelmed and anxious all the time and don’t know where to turn."

Expected Category:
Mental Health Services

Expected Escalation:
Human review REQUIRED
