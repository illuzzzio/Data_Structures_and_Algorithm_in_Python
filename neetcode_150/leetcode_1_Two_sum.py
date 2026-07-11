array = [1,2,4,56,6,7]
target = 62 

def two_Sum(array,target):
    hashmap = {}
    for key,value in enumerate(array):
        difference = target - value 
        if difference in hashmap:
            return [hashmap[difference],key]
        else:
            hashmap[value] = key 

print(two_Sum(array,target))