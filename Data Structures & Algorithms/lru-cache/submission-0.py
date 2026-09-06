class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")

        self._capacity = capacity
        self._cache= OrderedDict()

    def get(self, key: int) -> int:
        try:
            value = self._cache.pop(key)
        except KeyError:
            return -1

        self._cache[key] = value
        return value       

    def put(self, key: int, value: int) -> None:
        
        self._cache.pop(key, None)
        self._cache[key] = value

        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)