array = [1,2,3,6]

def product_except_self(array):
    result = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if j!=i:
                product *=array[j]
        result.append(product)
    return result 

print(product_except_self(array))