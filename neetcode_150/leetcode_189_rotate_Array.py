class Solution:
    def rotate(self, nums: list[int], k: int) -> None:




        n = len(nums)
        k = k%n
        arr = []
        for i in range(n-k,n):
            arr.append(nums[i])
        for i in range(0,n-k):
            arr.append(nums[i])
        nums[:] = arr
        return arr 
        # n = len(nums)
        # k = k%n
        # nums[:]=nums[-k:]+nums[:-k]
        # return nums

      # another approach 