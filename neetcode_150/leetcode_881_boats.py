people = [1,2,2,3]
limit = 3 

def valid_boat(people,limit):
    people.sort()
    left = 0
    boat = 0
    right = len(people)-1
    while(right>=left):
        if people[left]+people[right]<=limit:
            left+=1
        right-=1
        boat+=1
    return boat 

print(valid_boat(people,limit))


# 1+3 <=4 it means heaviest person has to go alone means not execute left+=1 only boat+=1 and right -=1 