from typing import TypedDict, List


class GraphState(TypedDict):

    query: str

    retrieved_docs: List[str]

    context: str

    evaluation: str

    final_answer: str