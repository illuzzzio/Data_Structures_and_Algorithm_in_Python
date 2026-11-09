class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        left = 0 
        right = len(matrix[0])-1

        while(top<=bottom):
            row = (top+bottom)//2
            if(target>matrix[row][-1]):
                top = row +1
            elif(target<matrix[row][0]):
                bottom = row-1
            else:
                break
        # now to initilisze same inside another loop

        row = (top+bottom)//2

        while(right>=left):
            mid = (left+right)//2
            if(target<matrix[row][mid]):
                right = mid-1
            elif(target>matrix[row][mid]):
                left = mid+1
            else:
                return True 
        return False 
        