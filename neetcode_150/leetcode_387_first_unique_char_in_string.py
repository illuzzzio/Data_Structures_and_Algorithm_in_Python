class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]]= hashmap.get(s[i],0)+1
        for index, value in enumerate(s):
            if hashmap[value] ==1:
                return index
        return -1 

