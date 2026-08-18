class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        mount = 0 
        result = 0
        if(len(arr)<3):
            return 0 

        else:
            for i in range(1,len(arr)-1):
                if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
                    left = right = i

                    while(left>0 and arr[left]>arr[left-1]):
                        left-=1
                    while(right+1<len(arr) and arr[right]>arr[right+1]):
                        right+=1
                    result = max(result,(right-left+1))
            return result 
       