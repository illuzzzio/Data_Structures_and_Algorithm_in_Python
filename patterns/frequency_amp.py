hashmap = {}
s = [1,2,3,4,5]

for i in s:
    if i in s :
        key = "".join(sorted(s))
        if key not in hashmap:
            hashmap[key] = 1
        hashmap[key].append(i)


     