import time

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.timestamps = []
    
    def __call__(self, func):
        def wrapped(*args, **kwargs):
            now = time.time()
            self.timestamps = [t for t in self.timestamps if t > now - self.period]
            
            if len(self.timestamps) >= self.max_calls:
                sleep_time = self.period - (now - self.timestamps[0])
                time.sleep(sleep_time)
            
            result = func(*args, **kwargs)
            self.timestamps.append(time.time())
            return result
        return wrapped