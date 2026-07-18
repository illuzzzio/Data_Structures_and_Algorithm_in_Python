arr = [1,2,5,43,64,43,4]
k = 4

def product(arr,k):
    max_sum = float("-inf")
    for i in range(len(arr)-k+1):
        current = 1 
        for j in range(i,i+k):
            current *=arr[j]
        if(current>max_sum):
            max_sum = current 
    return max_sum
print(product(arr,k))
        