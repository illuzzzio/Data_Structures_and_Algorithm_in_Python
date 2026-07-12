string = "pranjal"

def reverse_string(string):
    new_op = list(string)
    left = 0
    right = len(new_op)-1
    while(right>left):
        new_op[left], new_op[right] = new_op[right],new_op[left]

        left+=1
        right-=1
    return "".join(new_op)
print(reverse_string(string))