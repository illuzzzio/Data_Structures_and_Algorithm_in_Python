class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_number = bin(n)[2:]
        new_number = str(binary_number)
        count = 0 
        for i in new_number:
            if(i=="1"):
                count+=1
        return count 