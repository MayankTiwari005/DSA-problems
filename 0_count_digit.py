# count digit:
# n = 314879


def func(n):
    cnt = 0
    while n > 0:
        cnt += 1 
        n = n//10
    return cnt


