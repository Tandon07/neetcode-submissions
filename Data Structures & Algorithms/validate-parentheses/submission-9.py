class Solution:
    def isValid(self, s: str) -> bool:
        d={
            ")":"(",
            "]":"[",
            "}":"{"
        }

        ans=[]
        i=0
        if len(s)==1:
            return False
        for i in s:
            if i in d.values():
                ans.append(i)
            elif i in d:
                if not ans or ans[-1] != d[i]:
                    return False

                ans.pop()
            else:
                return False

        if len(ans)==0:
            return True
        else:
            return False