class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0 
        longest = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right],0)+1

            while((right-left+1)-max(hashmap.values())>k):
                hashmap[s[left]]-=1
                left+=1
            longest = max(longest,right-left+1)
        return longest     