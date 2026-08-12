class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)-1):
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                res=nums[i]+nums[left]+nums[right]
                if res==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif res>0:
                    right-=1
                elif res<0:
                    left+=1
        return result  