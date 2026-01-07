# PLAINDROME DIGIT PROGRAMMING
'''
n = 1221
num = n
result = 0      #6
while num > 0:
    ld = num % 10     # 6
    result = (result*10) + ld
    num = num // 10   #12345
if result == n:
    print(True)
else:
    print(False)
'''

def func(n, num, result=0):

    if num == 0:
        return result == n
    
    ld = num % 10
    return func(n, num//10, (result*10)+ld)


n = 1221
num = n
print(func(n,num,result=0))