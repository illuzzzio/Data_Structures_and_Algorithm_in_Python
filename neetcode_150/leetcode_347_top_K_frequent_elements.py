nums = [1,1,2,2,2,2,4,4,4]
k = 3 

def top_k(nums,k):
    hashmap= {}
    for c in range(len(nums)):
        hashmap[nums[c]] = hashmap.get(nums[c],0)+1

    # top_k_sorted = sorted(hashmap) # this only sort keys not the value but we need to sort keys acording to different attribute it an be length or some value here it is .get value 

    sorted_k_elements = sorted(hashmap, key=hashmap.get, reverse= True)

    return sorted_k_elements[:k]

print(top_k(nums,k))