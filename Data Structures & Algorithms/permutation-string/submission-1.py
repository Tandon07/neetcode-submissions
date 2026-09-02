class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for char in s1:
            need[ord(char) - ord("a")] += 1

        window_size = len(s1)

        for right, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1

            # Keep the window exactly len(s1) characters long.
            if right >= window_size:
                left_char = s2[right - window_size]
                window[ord(left_char) - ord("a")] -= 1

            if window == need:
                return True

        return False

