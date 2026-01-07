# gcf of 2 nos:
# 20: 1,2,4,5,10,20
# 28: 1,22,4,7,14,28
# gcd: 4

def brute(n1,n2):
    gcd = 0
    mini = min(n1,n2)
    for i in range(0, mini):
        if n1 % i == n2 % i:
            gcd = i
    return gcd

def better(n1, n2):
    gcd = 0
    mini = min(n1,n2)
    for i in range(mini, 0, -1):
        if n1 % i == n2 % i:
            return i
        

