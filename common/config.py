"""Shared configuration and model factories for the RAG / Agentic AI courses.

Every notebook in this repo needs the same three things: the `.env` loaded, a
chat model, and an embedding model. Rather than repeat that setup in each lab,
import it from here:

    import sys; sys.path.append("..")          # from inside a course folder
    from common.config import get_llm, get_embeddings

    llm = get_llm()                             # default provider
    emb = get_embeddings()                      # local, no API key needed

Provider imports are deliberately lazy: a missing `langchain-ibm` should only
break the watsonx path, not the whole module.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE, override=False)

DATA_DIR = PROJECT_ROOT / "data"
CHROMA_DIR = Path(os.getenv("CHROMA_PERSIST_DIR", PROJECT_ROOT / "chroma_db"))
FAISS_DIR = Path(os.getenv("FAISS_INDEX_DIR", PROJECT_ROOT / "faiss_index"))


def ensure_dirs() -> None:
    """Create the local data / index directories if they don't exist."""
    for path in (DATA_DIR, CHROMA_DIR, FAISS_DIR):
        path.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------
# Environment
# --------------------------------------------------------------------------


def get_env(key: str, default: str | None = None, *, required: bool = False) -> str | None:
    """Read an environment variable, with a clear error when a key is missing."""
    value = os.getenv(key, default)
    if required and not value:
        raise RuntimeError(
            f"Missing required environment variable {key!r}. "
            f"Copy .env.example to .env and fill it in."
        )
    return value


def available_providers() -> dict[str, bool]:
    """Which providers have credentials configured. Handy as a first notebook cell."""
    return {
        "watsonx": bool(os.getenv("WATSONX_APIKEY") and os.getenv("WATSONX_PROJECT_ID")),
        "openai": bool(os.getenv("OPENAI_API_KEY")),
        "huggingface": bool(os.getenv("HUGGINGFACEHUB_API_TOKEN")),
        "groq": bool(os.getenv("GROQ_API_KEY")),
    }


DEFAULT_PROVIDER = os.getenv("DEFAULT_LLM_PROVIDER", "watsonx")

DEFAULT_MODELS = {
    "watsonx": "meta-llama/llama-3-3-70b-instruct",
    "openai": "gpt-4o-mini",
    "groq": "llama-3.3-70b-versatile",
}

DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# --------------------------------------------------------------------------
# Model factories
# --------------------------------------------------------------------------


def get_llm(
    provider: str | None = None,
    model: str | None = None,
    *,
    temperature: float = 0.0,
    max_tokens: int = 1024,
    **kwargs: Any,
):
    """Return a LangChain chat model for the given provider.

    provider: "watsonx" | "openai" | "groq". Defaults to DEFAULT_LLM_PROVIDER.
    """
    provider = (provider or DEFAULT_PROVIDER).lower()
    model = model or DEFAULT_MODELS.get(provider)

    if provider == "watsonx":
        from langchain_ibm import ChatWatsonx

        return ChatWatsonx(
            model_id=model,
            url=get_env("WATSONX_URL", "https://us-south.ml.cloud.ibm.com"),
            apikey=get_env("WATSONX_APIKEY", required=True),
            project_id=get_env("WATSONX_PROJECT_ID", required=True),
            params={"temperature": temperature, "max_new_tokens": max_tokens},
            **kwargs,
        )

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            api_key=get_env("OPENAI_API_KEY", required=True),
            **kwargs,
        )

    if provider == "groq":
        from langchain_groq import ChatGroq

        return ChatGroq(
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            api_key=get_env("GROQ_API_KEY", required=True),
            **kwargs,
        )

    raise ValueError(
        f"Unknown provider {provider!r}. Expected one of: {', '.join(DEFAULT_MODELS)}"
    )


def get_embeddings(model: str | None = None, *, provider: str = "huggingface", **kwargs: Any):
    """Return a LangChain embeddings model.

    Defaults to a local sentence-transformers model so retrieval labs run
    offline and without burning API credits.
    """
    provider = provider.lower()

    if provider == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings(
            model_name=model or DEFAULT_EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
            **kwargs,
        )

    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings

        return OpenAIEmbeddings(
            model=model or "text-embedding-3-small",
            api_key=get_env("OPENAI_API_KEY", required=True),
            **kwargs,
        )

    if provider == "watsonx":
        from langchain_ibm import WatsonxEmbeddings

        return WatsonxEmbeddings(
            model_id=model or "ibm/slate-125m-english-rtrvr",
            url=get_env("WATSONX_URL", "https://us-south.ml.cloud.ibm.com"),
            apikey=get_env("WATSONX_APIKEY", required=True),
            project_id=get_env("WATSONX_PROJECT_ID", required=True),
            **kwargs,
        )

    raise ValueError(f"Unknown embeddings provider {provider!r}.")


if __name__ == "__main__":
    print(f"Project root : {PROJECT_ROOT}")
    print(f".env found   : {ENV_FILE.exists()}")
    print(f"Default LLM  : {DEFAULT_PROVIDER} -> {DEFAULT_MODELS.get(DEFAULT_PROVIDER)}")
    print("Credentials  :")
    for name, ok in available_providers().items():
        print(f"  {'OK ' if ok else '-- '} {name}")
