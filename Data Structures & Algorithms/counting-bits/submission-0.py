class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            c=0
            while i:
                i= i & (i-1)
                c=c+1
            res.append(c)
        return res