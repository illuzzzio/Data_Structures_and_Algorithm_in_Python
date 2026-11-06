class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        new_str = " ".join(words[::-1])
        return new_str 
