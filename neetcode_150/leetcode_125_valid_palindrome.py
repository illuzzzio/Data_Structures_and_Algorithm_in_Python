class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        result = ""
        char = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in x:
            if i in char:

                result+=i
        if(result==result[::-1]):
            return True
        else:
            return False 
        