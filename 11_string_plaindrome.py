# palindomr exist if the stirng read same from each side


s = "ANBCDDCBNA"
n = len(s)
print(n)
left = 0
right = n-1
is_palindrome = True                # Initially assume true
while left<right:
    if s[left] != s[right]:
        is_palindrome = False       # change value if found otherwise jumps this condition
       # print(False)               # break to stop
        break
    left += 1
    right -= 1
print(is_palindrome)                # final output