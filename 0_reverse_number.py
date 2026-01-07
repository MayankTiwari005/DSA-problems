# reverse number:
# 12345 to 54321

def func(num):
    cnt = 0
    new_num = 0
    while num > 0:
        last_digit = num % 10
        new_num = (new_num*10) + last_digit
        num = num//10
    return new_num