class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        result = []
        minimum = float("inf")
        
        for i in range(1,len(arr)):
            minimum = min(minimum, abs(arr[i]-arr[i-1]))
        for i in range(1,len(arr)):
            if(arr[i]-arr[i-1]==minimum):
                result.append([arr[i-1],arr[i]])
        return result 
       