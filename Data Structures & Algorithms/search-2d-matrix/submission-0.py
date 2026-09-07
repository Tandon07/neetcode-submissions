class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows= len(matrix)
        cols= len(matrix[0])

        for i in range(rows):
            if target<=matrix[i][cols-1]:
                l=0
                r=cols
                while l<=r:
                    mid= l+(r-l)//2
                    if matrix[i][mid]==target:
                        return True
                    if matrix[i][mid]<target:
                        l=mid+1
                    else:
                        r=mid-1
            else:
                continue
        return False


