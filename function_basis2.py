# 1
def countdown(num):
    numList = []
    for x in range(num+1):
        numList.append(num)
        num -=1
    return(numList)
print(countdown(5))
# 2
def printandreturn(group):
    print(group[0])
    return(group[1])
list = [4, 9]
print (printandreturn(list))
# 3
def firstpluslength(list):
    output = len(list) + list[0]
    return(output)
print (firstpluslength([5,1,2,5,2]))
# 4
def valuesgreaterthansecond(x):
    y = []
    for i in range(len(x)):
        if x[i]>x[1]:
            y.append(x[i])
    print(len(y))
    return(y)
list = [0,5,1,2,9,8,19]
print(valuesgreaterthansecond(list))
# 5
def length_and_value(x,y):
    list = []
    for x in range(x):
        list.append(y)
    return list
print(length_and_value(5,10))