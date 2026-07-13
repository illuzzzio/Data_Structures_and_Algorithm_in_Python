class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0)+1
        sorted_word = sorted(hashmap,key=hashmap.get,reverse = True)
        return "".join(char*hashmap[char] for char in sorted_word)
        