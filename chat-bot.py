import argparse

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

import os
import time

load_dotenv()

_OVH_AI_ENDPOINTS_ACCESS_TOKEN = os.environ.get("_OVH_AI_ENDPOINTS_ACCESS_TOKEN")
_OVH_AI_ENDPOINTS_MODEL_NAME = os.environ.get("_OVH_AI_ENDPOINTS_MODEL_NAME")
_OVH_AI_ENDPOINTS_URL = os.environ.get("_OVH_AI_ENDPOINTS_URL")


def chat_completion(question: str):
    model = ChatMistralAI(
        model=_OVH_AI_ENDPOINTS_MODEL_NAME,
        api_key=_OVH_AI_ENDPOINTS_ACCESS_TOKEN,
        endpoint=_OVH_AI_ENDPOINTS_URL,
        max_tokens=1500,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are Nestor, a virtual assistant. Answer to the question."),
            ("human", "{question}"),
        ]
    )

    chain = prompt | model

    response = chain.invoke(question)

    print(f"🤖: {response.content}")


def chat_completion_stream(new_message: str):
    model = ChatMistralAI(
        model=_OVH_AI_ENDPOINTS_MODEL_NAME,
        api_key=_OVH_AI_ENDPOINTS_ACCESS_TOKEN,
        endpoint=_OVH_AI_ENDPOINTS_URL,
        max_tokens=1500,
        streaming=True,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a Nestor, a virtual assistant. Answer to the question.",
            ),
            ("human", "{question}"),
        ]
    )

    chain = prompt | model

    print("🤖: ")
    for r in chain.stream({"question", new_message}):
        print(r.content, end="", flush=True)
        time.sleep(0.150)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--question", type=str, default="What is the meaning of life?")

    parser.add_argument(
        "--no-streaming",
        action="store_false",
        dest="streaming",
        help="Désactiver le streaming",
    )
    parser.set_defaults(streaming=True)

    args = parser.parse_args()

    if args.streaming:
        chat_completion_stream(args.question)
    else:
        chat_completion(args.question)


if __name__ == "__main__":
    main()
