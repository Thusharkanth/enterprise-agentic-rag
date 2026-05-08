import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def extract_text(response):
    """
    Return displayable text from LangChain/Gemini responses.
    """
    content = response.content if hasattr(response, "content") else response

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_parts.append(block.get("text", ""))
            elif isinstance(block, str):
                text_parts.append(block)

        return "\n".join(part for part in text_parts if part).strip()

    return str(content)


def get_llm():

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        temperature=0.3,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    return llm


if __name__ == "__main__":

    llm = get_llm()

    response = llm.invoke(
        "What is retrieval augmented generation?"
    )

    print("\n========== GEMINI RESPONSE ==========\n")

    # Clean output
    print(extract_text(response))
