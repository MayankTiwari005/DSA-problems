# SHEET ABOUT DIGITS MAJORLY
# extraction of digits
# check palindrome 
# Reverse a number
# check armstrong number


# remiander is the last digit you get for reversal or similar things (division by 10)

n = 5873
count = 0
num = n
while num>0:
    last_digit = num % 10       # 3
    print(last_digit)
    num=num//10                 # 587
    count+=1

count += 1
print(count)
