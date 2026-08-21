class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s: # as we already used set of nums 
            if(i-1) not in s:
                length = 0
                while(i+length in s):
                    length+=1
                longest = max(longest,length)
        return longest 
      
