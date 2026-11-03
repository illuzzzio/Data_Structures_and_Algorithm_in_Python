class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        
        total = 0
        for i in nums:
            result = abs(median-i)
            total+=result 
        return total 