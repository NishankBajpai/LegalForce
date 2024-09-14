import redis

# Connect to Redis
cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_document(key, document):
    cache.set(key, document, ex=3600)  # Cache expires in 1 hour

def get_cached_document(key):
    return cache.get(key)
