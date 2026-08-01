class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        res=[]
        for i,num in enumerate(nums):
            comp=target-num
            if num in l:
                return[l.get(num), i]
            l[comp]=i
