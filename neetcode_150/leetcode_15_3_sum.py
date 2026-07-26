class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i,v in enumerate(nums):
            if(i>0 and v==nums[i-1]):
                continue 
            left,right = i+1,len(nums)-1
            while(right>left):
                threesum = (v+nums[left]+nums[right])
                if(threesum>0):
                    right-=1
                elif(threesum<0):
                    left+=1
                else:
                    result.append([v,nums[left],nums[right]])
                    left+=1
                    right-=1

                    # skip duplicates 
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result 