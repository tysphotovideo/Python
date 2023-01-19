def countdown(num):
    cd = []
    for x in range(num, -1, -1):
        cd.append(x)  
    return cd        
print(countdown(10))

def printReturn(numList):
    print(numList[0])
    return numList[1]
number = [1,3]
printReturn(number)
print(printReturn(number))

def firstPlusLength(numlist1):
    sum = numlist1[0] + len(numlist1)
    return sum
first = [5,7,3,8]   

print(firstPlusLength(first))
      
def valueGreatSec(numlist2):
    if len(numlist2) < 2:
        return False
    count = 0
    greaterThan = []
    for x in range(0, len(numlist2)):
        if numlist2[x] > numlist2[1]:
            count +=1
            greaterThan.append(numlist2[x]) 
    print(count)    
    return greaterThan    
second = [5,4,3,6,8]
falseySec = []  

print(valueGreatSec(second))
print(valueGreatSec(falseySec))

def thisLenThatVal(s,v):
    thisThat = []
    for x in range(0, s):
        thisThat.append(v)
    return thisThat

print(thisLenThatVal(8,5))    
        

    