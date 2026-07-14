s = "aabc"
def twice(s):
    seen = []
    for i in s:
        if i in seen:
            return i
        seen.append(i)
print(twice(s))