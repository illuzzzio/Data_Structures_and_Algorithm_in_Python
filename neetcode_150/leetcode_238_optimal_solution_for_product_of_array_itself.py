class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        postfix =1 
        prefix = 1
        result = [1]*n
        for i in range(0,len(nums)):
            result[i]= prefix 
            prefix = prefix*nums[i]
        for i in range(n-1,-1,-1):
            result[i]= result[i]*postfix 
            postfix = postfix*nums[i]
        return result 

        # -1 as stop value so that the index 0 also got visited 
        

      