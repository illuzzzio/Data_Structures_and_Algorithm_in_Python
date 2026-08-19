class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        left = 0
        for right in range(len(nums)):
            if(abs(right-left)>k):
                #slide
                s.remove(nums[left])
                left+=1
            if(nums[right] in s):
                return True 
            s.add(nums[right])
        return False 
       