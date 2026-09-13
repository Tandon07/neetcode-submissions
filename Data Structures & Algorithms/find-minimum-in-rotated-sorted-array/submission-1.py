class Solution:
    from typing import Sequence


    def findMin(self, nums: Sequence[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]