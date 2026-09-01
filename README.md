# IBM RAG and Agentic AI Professional Certificate (Coursera)

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

![Courses](https://img.shields.io/badge/Courses-10-blue)

![Provider](https://img.shields.io/badge/Provider-IBM-red)

![Platform](https://img.shields.io/badge/Coursera-Certificate-0056D2)

> 🚧 **Currently in progress**
>
> ✔ 10 Courses
>
> ✔ Hands-on Labs
>
> ✔ Final Capstone Project

> A repository documenting my learning journey through the **[IBM RAG and Agentic AI Professional Certificate](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai)** on Coursera — notes, hands-on labs, assignments, experiments, mini-projects, and the final capstone.

This program is the follow-on to my completed **[IBM Generative AI Engineering Professional Certificate](../IBM_Generative_AI_Engineering)**, moving from model-centric work (training, fine-tuning, alignment) to **system-centric** work: retrieval pipelines, vector stores, tool-calling agents, multi-agent orchestration, and the Model Context Protocol.

---

# 🚀 Overview

The focus here is on building **production-shaped AI systems** rather than models:

- Grounding LLMs in private data with **Retrieval-Augmented Generation (RAG)**
- Designing and tuning **vector database** retrieval
- Giving models **tools**, **memory**, and **control flow** so they can act — not just answer
- Coordinating **multiple agents** with LangGraph, CrewAI, AutoGen (AG2) and BeeAI
- Exposing capabilities through the **Model Context Protocol (MCP)**

---

# 📚 Course Structure

| # | Course | Focus |
|---|--------|-------|
| 1 | Develop Generative AI Applications: Get Started | LLM app fundamentals, prompts, app scaffolding |
| 2 | Build RAG Applications: Get Started | Loaders, chunking, embeddings, first RAG pipeline |
| 3 | Vector Databases for RAG: An Introduction | Indexing, similarity search, Chroma / FAISS |
| 4 | Advanced RAG with Vector Databases and Retrievers | Advanced retrievers, re-ranking, evaluation |
| 5 | Build Multimodal Generative AI Applications | Text + image/audio inputs, multimodal prompting |
| 6 | Fundamentals of Building AI Agents | Tool calling, reasoning loops, agent design |
| 7 | Agentic AI with LangChain and LangGraph | Graph-based agent workflows, state, memory |
| 8 | Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI | Multi-agent orchestration across frameworks |
| 9 | Build AI Agents using MCP | Model Context Protocol servers, clients, tools |
| 10 | RAG and Agentic AI Capstone Project | End-to-end agentic RAG application |

---

# 🎯 Learning Objectives

- Build and deploy generative AI applications end to end
- Implement RAG pipelines: document loading, chunking, embedding, retrieval, generation
- Choose, configure and tune vector databases for retrieval quality
- Apply advanced retrieval strategies (hybrid search, re-ranking, query rewriting)
- Work with multimodal inputs and prompts
- Design agents with tool calling, planning, and memory
- Orchestrate multi-agent systems with LangGraph, CrewAI, AutoGen (AG2) and BeeAI
- Build and consume MCP servers to expose tools and data to agents
- Evaluate agentic and RAG systems for accuracy, cost, latency and safety
- Ship a complete capstone application

---

# 🧩 Topics Covered

## Retrieval-Augmented Generation (RAG)

- Document loaders & parsers (PDF, HTML, Markdown)
- Chunking and text splitting strategies
- Embedding models and embedding selection
- Semantic / similarity search
- Hybrid search and re-ranking
- Context construction and prompt stuffing
- Grounding, citations, and hallucination reduction
- RAG evaluation

## Vector Databases

- Vector indexes and distance metrics
- Chroma
- FAISS
- Milvus / Pinecone concepts
- Metadata filtering
- Persistence and index maintenance

## AI Agents

- Tool / function calling
- ReAct-style reasoning loops
- Planning and task decomposition
- Short-term and long-term memory
- Human-in-the-loop checkpoints
- Guardrails and failure handling

## Multi-Agent Orchestration

- LangGraph (state graphs, nodes, edges, checkpointing)
- CrewAI (roles, tasks, crews)
- AutoGen / AG2 (conversational agents)
- BeeAI
- Agent-to-agent communication patterns

## Model Context Protocol (MCP)

- MCP servers and clients
- Exposing tools, resources and prompts
- Connecting agents to external systems

## Multimodal GenAI

- Image and audio inputs
- Multimodal prompting
- Cross-modal retrieval

## Application Development

- Flask APIs
- Gradio interfaces
- Streaming responses
- Secrets and API key management
- Observability and tracing

---

# 🛠️ Technologies & Tools

### Languages

- Python

### LLM & Agent Frameworks

- LangChain
- LangGraph
- CrewAI
- AutoGen (AG2)
- BeeAI
- Model Context Protocol (MCP)

### Vector Databases

- Chroma
- FAISS

### Models & Providers

- IBM watsonx.ai
- OpenAI API
- Hugging Face Transformers / Sentence-Transformers

### Data & Documents

- Pandas
- NumPy
- pypdf / PyMuPDF
- BeautifulSoup

### Interfaces & Serving

- Gradio
- Flask

### Development Tools

- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 📂 Repository Structure

Each course is broken down module by module, with the notebooks, cheat sheets,
glossaries and reading material for that module kept together:

```text
<N>. Course Name/
    1. Module Name/
        <lab>.ipynb
        Cheat Sheet- <topic>.pdf
        Glossary- <topic>.pdf
        <diagram>.png
        <dataset>.txt
    2. Module Name/
        ...
    Course Conclusion.pdf

common/                 # shared config: env loading, LLM & embedding factories
requirements.txt        # pip dependencies
environment.yml         # conda env recipe (Python 3.12)
.env.example            # template for API keys — copy to .env
```

The ten course folders:

```text
1. Develop Generative AI Applications- Get Started/
2. Build RAG Applications- Get Started/
3. Vector Databases for RAG- An Introduction/
4. Advanced RAG with Vector Databases and Retrievers/
5. Build Multimodal Generative AI Applications/
6. Fundamentals of Building AI Agents/
7. Agentic AI with LangChain and LangGraph/
8. Agentic AI with LangGraph, CrewAI, AutoGen and BeeAI/
9. Build AI Agents using MCP/
10. RAG and Agentic AI Capstone Project/
```

---

# ⚙️ Setup

```bash
python -m venv myenv
```

```bash
myenv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root (it is git-ignored) for your API keys:

```text
OPENAI_API_KEY=...
WATSONX_APIKEY=...
WATSONX_PROJECT_ID=...
HUGGINGFACEHUB_API_TOKEN=...
```

---

# 🚀 Capstone Project

The program concludes with an end-to-end **RAG + Agentic AI** application combining
retrieval over private documents with a tool-using, multi-step agent.

Planned stack:

- Python
- LangChain + LangGraph
- Chroma / FAISS
- watsonx.ai / OpenAI models
- MCP tools
- Gradio or Flask interface

---

# 📈 Skills Being Developed

- Retrieval-Augmented Generation (RAG)
- Vector Databases & Semantic Search
- Embeddings & Re-ranking
- Prompt Engineering
- Tool Calling
- AI Agent Design
- Multi-Agent Orchestration
- LangChain / LangGraph / CrewAI / AutoGen / BeeAI
- Model Context Protocol (MCP)
- Multimodal Prompting
- LLM Application Development
- AI Security & Guardrails
- Python Programming

---

# 🎓 Certification

**IBM RAG and Agentic AI Professional Certificate**

Provider:

- IBM
- Coursera

Status:

**In Progress 🚧**

---

# 🤝 Connect

If you're interested in RAG, AI agents, multi-agent systems, or LLM application development, feel free to connect or discuss ideas.

---

## ⭐ Support

If you found this repository useful or informative, consider giving it a **Star ⭐**.
