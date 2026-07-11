given = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(given):
    hashmap = {}
    for word in given:
        key = "".join(sorted(word)) # aet 
        if key not in hashmap:
            hashmap[key] = []
        hashmap[key].append(word)
    return list(hashmap.values())

print(group_anagrams(given))