import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            if  timestamp in self.store[key]:
                return self.store[key][timestamp]
            else:
                while timestamp >=0:
                    if timestamp in self.store[key]:
                        return self.store[key][timestamp]
                    timestamp -= 1
        return "" 
