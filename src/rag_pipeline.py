# RAG pipeline scaffold
# This file will handle document loading, retrieval, and prompt grounding

import os

def load_documents(data_folder_path):
    """
    Loads all .txt documents from the data folder.
    Returns a list of dictionaries with filename and content.
    """
    documents = []

    for filename in os.listdir(data_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(data_folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                documents.append({
                    "source": filename,
                    "content": content
                })

    return documents


def retrieve_documents(query, documents):
    """
    Retrieves documents that contain the query keyword.
    Returns a list of matching documents.
    """
    query_lower = query.lower()
    matched_documents = []

    for doc in documents:
        if query_lower in doc["content"].lower():
            matched_documents.append(doc)

    return matched_documents


def build_grounded_prompt(query, retrieved_documents):
    """
    Builds a prompt that grounds the query in retrieved documents.
    """
    context_blocks = []

    for doc in retrieved_documents:
        block = f"Source: {doc['source']}\n{doc['content']}"
        context_blocks.append(block)

    context_text = "\n\n---\n\n".join(context_blocks)

    prompt = f"""
You are an AI assistant supporting higher-education staff.

Use ONLY the information provided in the context below.
Do NOT invent policies or procedures.

Context:
{context_text}

Student Question:
{query}

Task:
Provide a short, staff-facing summary grounded in the provided context.
"""

    return prompt


if __name__ == "__main__":
    documents = load_documents("../data")

    query = "Why was my financial aid reduced?"
    retrieved = retrieve_documents("financial aid", documents)

    prompt = build_grounded_prompt(query, retrieved)

    print("=== GROUNDED PROMPT ===")
    print(prompt)
