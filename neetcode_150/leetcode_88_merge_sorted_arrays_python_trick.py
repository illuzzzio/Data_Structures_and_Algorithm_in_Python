class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        return nums1
        
        return
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        