class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap ={}
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
        for i,v in enumerate(nums):
            if hashmap[v]==1:
                return v
        return 1
