def maximum_subarray_sum(arr,k):
    maximum_sum = float("-inf")
    for i in range(len(arr)-k+1):
        current_sum = 0
        for j in range(i,i+k):
            current_sum+=arr[j]
        if(current_sum>maximum_sum):
            maximum_sum = current_sum
    return maximum_sum

arr = [1,2,5,43,64,43,4]
k = 4
print(maximum_subarray_sum(arr,k))



# more optimal solution using sliding window technique


            
