array = [1,2,4,56,6,7]


def duplicates(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:
                return True 
    return False 

print(duplicates(array))



# for optimal approach we will sue set 
def optimal_duplicates(array):
    new_array = set(array)
    if len(new_array)== len(array):
        return False 
    else :
        return True 
    
print(optimal_duplicates(array))