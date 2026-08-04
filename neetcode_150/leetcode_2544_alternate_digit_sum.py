class Solution:
    def alternateDigitSum(self, n: int) -> int:
        new_num = str(n)

        sum = 0
        for i in range(0,len(new_num)):
            if (i%2==0):
                sum+=int(new_num[i])
            else:
                sum-=int(new_num[i])
        return sum
        