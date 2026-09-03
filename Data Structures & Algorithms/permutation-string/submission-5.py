class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l=0
        r=len(s1)
        d_s1={}
        d_s2={}
        for i in s1:
            if i not in d_s1:
                d_s1[i]=1
            else:
                d_s1[i]+=1

        for i in s2[0:len(s1)]:
            if i not in d_s2:
                d_s2[i]=1
            else:
                d_s2[i]+=1
        if d_s1==d_s2:
            return True

        for right in range(len(s1), len(s2)):
            # Character entering the window
            entering = s2[right]
            d_s2[entering] = d_s2.get(entering, 0) + 1

            # Character leaving the window
            leaving = s2[right - len(s1)]
            d_s2[leaving] -= 1

            if d_s2[leaving] == 0:
                del d_s2[leaving]

            if d_s1 == d_s2:
                return True

        return False                
                
