class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            if nums[i]>0:
                break 
            left = i+1
            right = n-1 
            while(right>left):
                threesum = nums[i]+nums[left]+nums[right]

                if(threesum>0):
                    right-=1
                elif(threesum<0):
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])

                    while(right>left and nums[left]==nums[left+1]):
                        left+=1
                    while(right>left and nums[right]==nums[right-1]):
                        right-=1
                    left+=1
                    right-=1
        return result 
           
