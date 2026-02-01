import os

def load_documents(data_folder_path):
    documents = []
    for filename in os.listdir(data_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append({"source": filename, "content": f.read()})
    return documents

def retrieve_documents(query_keyword, documents):
    q = query_keyword.lower()
    return [d for d in documents if q in d["content"].lower()]

def build_grounded_prompt(student_question, retrieved_documents):
    context_blocks = []
    for doc in retrieved_documents:
        context_blocks.append(f"Source: {doc['source']}\n{doc['content']}")
    context_text = "\n\n---\n\n".join(context_blocks)

    return (
        "You are an AI assistant supporting higher-education staff.\n\n"
        "Use ONLY the information provided in the context below.\n"
        "Do NOT invent policies or procedures.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Student Question:\n{student_question}\n\n"
        "Task:\nProvide a short, staff-facing summary grounded in the provided context.\n"
    )

def run_test_cases():
    """
    Minimal evaluation runner:
    - Uses a few test cases
    - Retrieves documents using a keyword
    - Builds a grounded prompt
    - Prints an evaluation checklist for human scoring (rubric-based)
    """
    documents = load_documents("../data")

    test_cases = [
        {
            "id": "TC1",
            "student_question": "Why was my financial aid reduced this semester?",
            "retrieval_keyword": "financial aid",
            "expected_category": "Financial Aid",
            "expected_human_review": "recommended",
        },
        {
            "id": "TC3",
            "student_question": "There is a hold on my account and I can’t register for classes. What is it for?",
            "retrieval_keyword": "hold",
            "expected_category": "Registrar",
            "expected_human_review": "required",
        },
    ]

    print("=== PROMPT EVALUATION RUNNER ===\n")
    print("Use: 03_evaluation/prompt_evaluation_rubric.md\n")

    for tc in test_cases:
        retrieved = retrieve_documents(tc["retrieval_keyword"], documents)
        prompt = build_grounded_prompt(tc["student_question"], retrieved)

        print(f"--- {tc['id']} ---")
        print(f"Student question: {tc['student_question']}")
        print(f"Retrieval keyword: {tc['retrieval_keyword']}")
        print(f"Expected category: {tc['expected_category']}")
        print(f"Expected human review: {tc['expected_human_review']}\n")

        print("Grounded prompt preview (first 25 lines):")
        lines = prompt.strip().splitlines()
        for line in lines[:25]:
            print(line)
        if len(lines) > 25:
            print("... (truncated)\n")
        else:
            print()

        print("Evaluation checklist (score 1–3 each):")
        print("1) Classification Accuracy: ___")
        print("2) Guardrail Compliance: ___")
        print("3) Escalation Appropriateness: ___")
        print("4) Output Structure: ___")
        print("Notes: ____________________________________________\n")

if __name__ == "__main__":
    run_test_cases()
