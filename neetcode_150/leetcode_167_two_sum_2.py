class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap ={}
        for i,v in enumerate(numbers):
            difference = target-v
            if difference in hashmap:
                return [hashmap[difference]+1,i+1]  # main logic is here, we are returning the index of the difference and the current index
            hashmap[v]= i
