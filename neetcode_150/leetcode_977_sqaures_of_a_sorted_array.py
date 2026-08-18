class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []
        for i in nums:
            sq = i*i
            final.append(sq)
        final.sort()
        return final 
        