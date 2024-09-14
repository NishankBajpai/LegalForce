# Document Retrieval System

This project is a document retrieval system for chat applications. It includes features like caching, semantic search using Pinecone, background news article scraping, rate-limiting, and Dockerization.

## Features
- **Full-text and Semantic Search**: Search documents using both traditional full-text search and embeddings-based semantic search.
- **Caching**: Redis-based caching for faster retrieval of repeated search queries.
- **Background Scraping**: A separate thread continuously scrapes news articles and stores them in the database.
- **Rate Limiting**: Limits the number of search requests a user can make in a day.
- **Dockerized**: The application is containerized using Docker for easy deployment.

## Prerequisites
- Python 3.8+
- Redis (for caching)
- Elasticsearch (for full-text search) or Pinecone (for vector search)
- Docker (optional, for running the app in a container)

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/NishankBajpai/LegalForce.git
cd repo-name
