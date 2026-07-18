class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(s==""):
            return 0
        left = 0 
        result = float("-inf")
        hashset = set()
        for right in range(len(s)):
            while(s[right] in hashset):
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            result = max(result,right-left+1)
        return result 