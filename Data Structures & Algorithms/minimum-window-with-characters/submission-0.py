from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_count = len(need)

        left = 0
        min_len = float("inf")
        min_left = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                window_len = right - left + 1

                if window_len < min_len:
                    min_len = window_len
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return "" if min_len == float("inf") else s[min_left:min_left + min_len]