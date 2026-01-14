# OVHcloud AI Endpoints Tutorials with LangChain

This repository contains exercises associated with three OVHcloud tutorials designed to teach you how to build advanced chatbots in Python using LangChain and OVHcloud **AI Endpoints**.

---

## 📚 Included Tutorials

1. **Simple Chatbot with LangChain**
   Based on the tutorial “Develop a chatbot in Python with LangChain” from OVHcloud.
   [Tutorial link](https://help.ovhcloud.com/csm/fr-public-cloud-ai-endpoints-chatbot-langchain?id=kb_article_view&sysparm_article=KB0067317)
   → Create a basic assistant connected to the AI Endpoints, capable of answering questions via the command line.

2. **Chatbot with Conversational Memory**
   Based on the tutorial “Enable conversational memory in your chatbot with LangChain”.
   [Tutorial link](https://help.ovhcloud.com/csm/fr-public-cloud-ai-endpoints-chatbot-memory-langchain?id=kb_article_view&sysparm_article=KB0067427)
   → Adds the ability for your chatbot to remember previous interactions, making conversations more coherent.

3. **RAG Chatbot (Retrieval-Augmented Generation)**
   Based on the tutorial “Develop a RAG chatbot with LangChain”.
   [Tutorial link](https://help.ovhcloud.com/csm/fr-public-cloud-ai-endpoints-rag-chatbot-langchain?id=kb_article_view&sysparm_article=KB0067423)
   → Build an advanced chatbot that uses a document base to improve the relevance of its answers.

---

## 🚀 Repository Structure

```

tuto_langchain_ovh/
├── chat-bot/
│   ├── chat-bot.py
│   ├── requirements.txt
├── chat-bot-rag/
│   ├── rag-files/
│   │   ├── joke.txt
│   ├── chat-bot-rag.py
│   ├── requirements.txt
├── chat-bot-with-memory/
│   ├── chat-bot-with-memory.py
│   ├── requirements.txt
└── README.md

```

Each subfolder contains:
- The complete Python code
- A `requirements.txt` file listing all necessary dependencies

---

## ⚙️ Prerequisites

Before getting started, make sure you have:

- Python **3.10.12**
- A Public Cloud project on OVHcloud
- An **AI Endpoints access token** (see the OVHcloud *Getting Started* guide to generate one)
- A `.env` file at the root of the repository or inside each tutorial folder, containing:

```env
OVH_AI_ENDPOINTS_ACCESS_TOKEN=<your_token>
OVH_AI_ENDPOINTS_MODEL_NAME=Mistral-7B-Instruct-v0.3
OVH_AI_ENDPOINTS_URL=https://oai.endpoints.kepler.ai.cloud.ovh.net/v1
OVH_AI_ENDPOINTS_EMBEDDING_MODEL_NAME=bge-m3
```
