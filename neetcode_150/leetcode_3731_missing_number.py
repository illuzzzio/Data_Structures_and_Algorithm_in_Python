class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        for i in range(nums[0],nums[-1]):
            if i not in  nums:
                result.append(i)
        return result 