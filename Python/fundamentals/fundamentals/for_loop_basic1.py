for x in range(0, 151):
    print(x)
for x in range(5, 1001, 5):
    print(x)
for x in range(1,101):
    y = "Coding"
    z = "Coding Dojo"
    if x % 10 == 0:
        print(z)
    elif x % 5 == 0:
        print(y)
    else:
        print(x)
def oddSum (n):
    sum = 0
    for x in range(0, n):
        if x % 2 == 1:
            sum += x
    return sum
print(oddSum(500000))
for x in range(2018, 0, -4):
    print(x)
def flexNum(lowNum, highNum, mult):
    for x in range(lowNum, highNum+1):
        if x % mult == 0:
            print(x)
flexNum(1, 25, 5)








