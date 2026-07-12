data = [1,2,3]
hashmap = {}
for i in data:
    if i not in hashmap:
        hashmap[i] = 1
    hashmap[i]+=1