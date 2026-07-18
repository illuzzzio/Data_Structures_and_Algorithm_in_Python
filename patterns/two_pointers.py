name = "pranjal"
def reverse(name):
    new_name = list(name)
    left = 0
    right = len(new_name)-1
    while(right>left):
        new_name[left], new_name[right]= new_name[right], new_name[left]
        left+=1
        right-=1
    return "".join(new_name)

print(reverse(name))


