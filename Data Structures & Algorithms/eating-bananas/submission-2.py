class Solution:
    from typing import List


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            raise ValueError("piles must not be empty")
        if h <= 0:
            raise ValueError("h must be positive")
        if any(not isinstance(pile, int) or pile <= 0 for pile in piles):
            raise ValueError("piles must contain positive integers")
        if h < len(piles):
            raise ValueError("h must be at least the number of piles")

        def hours_required(k: int) -> int:
            # ceil(pile / k) without floating-point arithmetic.
            return sum((pile + k - 1) // k for pile in piles)

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if hours_required(mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left