class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        res=s[0]
        l=0
        r=1
        lon=len(res)
        while r<len(s):
            if s[r] not in res:
                res+=s[r]
                r+=1
                lon=max(lon, len(res))
            else:
                l+=1
                res=res[1:]
                
        return lon