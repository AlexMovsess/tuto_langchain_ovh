## Needs requirements1.txt

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

load_dotenv()

ai_endpoint_token = os.getenv("_OVH_AI_ENDPOINTS_ACCESS_TOKEN")
ai_endpoint_url = os.getenv("_OVH_AI_ENDPOINTS_URL")

llm = ChatOpenAI(
    model_name="Mistral-7B-Instruct-v0.3",
    openai_api_key=ai_endpoint_token,
    openai_api_base=ai_endpoint_url,
    max_tokens=512,
    temperature=0.0,
)

memory = ConversationBufferWindowMemory(k=10)

conversation = ConversationChain(llm=llm, memory=memory)

question = "Hello, my name is Alex"
response = conversation.predict(input=question)
print(f"👤: {question}")
print(f"🤖: {response}")

question = "What is the capital of France?"
response = conversation.predict(input=question)
print(f"👤: {question}")
print(f"🤖: {response}")

question = "Do you know my name?"
response = conversation.predict(input=question)
print(f"👤: {question}")
print(f"🤖: {response}")

question = "What was my precedent question?"
response = conversation.predict(input=question)
print(f"👤: {question}")
print(f"🤖: {response}")
