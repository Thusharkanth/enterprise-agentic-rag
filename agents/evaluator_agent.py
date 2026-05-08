from services.llm import get_llm


def evaluate_context(query, context):
    """
    Evaluate whether retrieved context is sufficient.
    """

    with open("prompts/evaluator_prompt.txt", "r", encoding="utf-8") as file:
        prompt_template = file.read()

    prompt = prompt_template.format(query=query, context=context)

    llm = get_llm()

    response = llm.invoke(prompt)

    # Safe extraction
    if hasattr(response, "content"):
        content = response.content

        if isinstance(content, list):
            evaluation = content[0]["text"].strip().lower()

        else:
            evaluation = str(content).strip().lower()

    else:
        evaluation = str(response).strip().lower()

    print("\n========== EVALUATOR RESULT ==========")
    print(evaluation)

    return evaluation


if __name__ == "__main__":
    query = "How should employees report security incidents?"

    context = """
    Employees must report security incidents immediately.

    Reporting channels:
    - security@nexacore.com
    - Slack #security-incidents
    - Hotline ext. 9911
    """

    result = evaluate_context(query, context)

    print("\n========== FINAL DECISION ==========")
    print(result)
