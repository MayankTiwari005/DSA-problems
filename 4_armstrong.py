# ARMSTRONG NUMBER
# 153 = 1^3  +  5^3  +  3^3  = 153    :armstrong number

n = 153
num = n
nod = len(str(n))
arm = 0
while num > 0 :
    ld = num % 10
    arm += ld**nod
    num = num // 10
print(arm)
if arm == n:
    print(True)
else:
    print(False)