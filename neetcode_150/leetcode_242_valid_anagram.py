from collections import Counter 
s = "pranjal"
t = "lajnarp"

def isvalid(s,t):
    hashmap_s = {}
    hashmap_t = {}
    if(len(s)!=len(t)):
        return False 
    else :
        for i in range(len(s)):
            hashmap_s[s[i]] = hashmap_s.get(s[i],0)+1
        for c in range(len(t)):
            hashmap_t[t[c]] = hashmap_t.get(t[c],0)+1
        if hashmap_s == hashmap_t:
            return True 
        else :
            return False 
    # return hashmap_s[s[i]] == hashmap_t[t[c]]


print(isvalid(s,t))
            

# more better for space is we can use i=single hashmap with two var 

def is_new_valid(s,t):
    count = {}
    for i in range(len(s)):
        count[s[i]] = count.get(s[i],0)+1
    for i in range(len(t)):
        count[t[i]] = count.get(t[i],0)-1
    for value in count.values():
        if value!= 0:
            return False 
    return True 

print(is_new_valid(s,t))

# if using fore i in s : use i and if usign for in range fucntion use s[i]