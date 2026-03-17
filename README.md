# RAG AI Chatbot using Endee Vector Database

## Overview
This project demonstrates a simple Retrieval Augmented Generation (RAG) style workflow using vector embeddings.

Documents are converted into embeddings and stored locally as vectors. When a user submits a query, the system retrieves the most relevant documents using cosine similarity.

## Features
- Semantic search
- Document retrieval
- Simple chatbot interface
- Vector embeddings

## Architecture
Documents → Embeddings → Vector Store → Query → Similarity Search → Response

## Setup

Install dependencies

pip install -r requirements.txt

Generate embeddings

python embed_store.py

Run application

python app.py


