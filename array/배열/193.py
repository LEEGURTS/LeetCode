def product(n: list[int]) -> list[int]:
    output = []
    productleft = [1]
    productright = [1]

    for i in range(len(n)-1):
        productleft.append(productleft[i]*n[i])
        productright.append(productright[i]*n[len(n)-1-i])

    for i in range(len(n)):
        output.append(productleft[i]*productright.pop())
    return output

arr=[1,2,3,4]
print(product(arr))