from redis import Redis

# Redis for storing user requests
redis = Redis()

def manage_user_requests(user_id):
    user_requests = redis.get(user_id)
    
    if user_requests is None:
        redis.set(user_id, 1, ex=86400)  # Set expiry for 24 hours
        return True
    else:
        request_count = int(user_requests)
        if request_count >= 5:
            return False
        redis.incr(user_id)
        return True
