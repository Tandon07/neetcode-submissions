
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key)

        if not values:
            return ""

        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            mid_timestamp, mid_value = values[mid]

            if mid_timestamp <= timestamp:
                # Valid candidate. But there may be a later
                # timestamp that is still <= the requested timestamp.
                result = mid_value
                left = mid + 1
            else:
                # This timestamp is too large.
                right = mid - 1

        return result

