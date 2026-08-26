class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        hashmap = {}
        maximum = float("-inf")
        

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right],0)+1
            while((right-left+1)-max(hashmap.values())>k):
                hashmap[s[left]]-=1
                left+=1
            maximum =  max(maximum,right-left+1)
        return maximum 

       