# FACTORS OF GIVEN NUMBER 

from math import sqrt


def fct(n):
    num = n
    result = []
    for i in range(1,num//2):
        if num % i == 0:
            result.append(i)

    result.append(num)
    print(result)
fct(1541)


def sqt(n):
    num = n
    result = []
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num//i)
    print(result)

sqt(36)



