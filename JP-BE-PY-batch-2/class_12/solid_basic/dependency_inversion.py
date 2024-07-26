# before
class RedisCache:
    def set(self, key, value):
        print(f"Setting {key} in Redis cache with value {value}")

    def get(self, key):
        print(f"Getting {key} from Redis cache")


class UserService:
    def __init__(self):
        self.cache = RedisCache()  # Direct dependency on RedisCache

    def store_user(self, user_id, user_data):
        self.cache.set(user_id, user_data)

    def retrieve_user(self, user_id):
        return self.cache.get(user_id)

# Usage Example
user_service = UserService()
user_service.store_user("user1", {"name": "Alice"})
user_service.retrieve_user("user1")




# after
from abc import ABC, abstractmethod

# Abstraction
class Cache(ABC):
    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

# Concrete Implementation 1: Redis
class RedisCache(Cache):
    def set(self, key, value):
        print(f"Setting {key} in Redis cache with value {value}")

    def get(self, key):
        print(f"Getting {key} from Redis cache")
        return f"Redis data for {key}"

# High-Level Module
class UserService:
    def __init__(self, cache: Cache):
        self.cache = cache

    def store_user(self, user_id, user_data):
        self.cache.set(user_id, user_data)

    def retrieve_user(self, user_id):
        return self.cache.get(user_id)

if __name__ == "__main__":
    
    # Usage Example
    redis_cache = RedisCache()

    user_service_redis = UserService(redis_cache)

    user_service_redis.store_user("user1", {"name": "Alice"})
    print(user_service_redis.retrieve_user("user1"))
