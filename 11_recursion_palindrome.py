def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s, left+1, right-1)

s = "nitin"
p = "mom"
l = "abcdef"
#n=len(s)
print(func(s,0,len(s)-1))
print(func(p,0,len(p)-1))
print(func(l,0,len(l)-1))