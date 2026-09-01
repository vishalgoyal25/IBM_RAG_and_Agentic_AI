"""Shared helpers reused across the course folders."""

from common.config import (
    CHROMA_DIR,
    DATA_DIR,
    FAISS_DIR,
    PROJECT_ROOT,
    available_providers,
    ensure_dirs,
    get_embeddings,
    get_env,
    get_llm,
)

__all__ = [
    "CHROMA_DIR",
    "DATA_DIR",
    "FAISS_DIR",
    "PROJECT_ROOT",
    "available_providers",
    "ensure_dirs",
    "get_embeddings",
    "get_env",
    "get_llm",
]
