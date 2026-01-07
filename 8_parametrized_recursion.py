
# PARAMETRIZED RECURSSION

def func(sum, i, n):
    if i>n:
        print(sum)
        return
    func(sum+i, i+1, n)

func(0,1,4)

'''
0,1,4
1,2,4
3,3,4
6,4,4
10,5,4 : print

'''

def f2(n):
    if 1>n:
        return
    print(n)
    f2(n-1)
f2(4)

def rec(z):
    if z==1:
        return 1
    return z + rec(z-1)
print(rec(4))
        