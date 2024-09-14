from elasticsearch import Elasticsearch
import pinecone

# Elasticsearch setup
es = Elasticsearch()

# Pinecone for vector storage
pinecone.init(api_key='95bf2a96-9552-45d4-9b10-f90ae8b05c06')
index = pinecone.Index('document-index')

def store_document(doc_id, text):
    # Index document in Elasticsearch
    es.index(index="documents", id=doc_id, body={"text": text})
    
    vector = encode_text_to_vector(text)  
    index.upsert([(doc_id, vector)])

def search_documents(query, top_k=5, threshold=0.8):
    # Full-text search in Elasticsearch
    results = es.search(index="documents", body={"query": {"match": {"text": query}}})
    
    query_vector = encode_text_to_vector(query)
    response = index.query(query_vector, top_k=top_k, filter={'score': {'gte': threshold}})
    return response['matches']
