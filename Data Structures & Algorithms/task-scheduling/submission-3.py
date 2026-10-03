from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(freq == max_freq for freq in counts.values())

        required = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), required)