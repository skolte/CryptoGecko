import pickle
import os
from datetime import datetime, timedelta

class CacheManager:
    def __init__(self, cache_dir=".cache", ttl=15):
        self.cache_dir = cache_dir
        self.ttl = timedelta(minutes=ttl)
        os.makedirs(cache_dir, exist_ok=True)
    
    def get(self, key):
        path = f"{self.cache_dir}/{key}.pkl"
        if not os.path.exists(path):
            return None
            
        with open(path, 'rb') as f:
            data, timestamp = pickle.load(f)
            if datetime.now() - timestamp > self.ttl:
                return None
            return data
    
    def set(self, key, data):
        path = f"{self.cache_dir}/{key}.pkl"
        with open(path, 'wb') as f:
            pickle.dump((data, datetime.now()), f)