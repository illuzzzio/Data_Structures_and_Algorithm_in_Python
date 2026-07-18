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
        

def optimal(arr,k):
    current_product = 1
    for i in range(0,k):
        current_product +=arr[i]
    max_product = current_product 
    for i in range(len(arr)-k):
        current_product /=arr[i]
        current_product *= arr[i+k]\
        
        if(current_product>max_product):
            max_product = current_product
    return max_product 
print(product(arr,k))

