# 5445, 76548, 1221

def func(num):
    temp = num
    new_num = 0
    while temp > 0:
        last_digit = temp % 10
        new_num = (new_num * 10) + last_digit
        temp = temp//10
    if new_num == num:
        return True
    else:
        print("not palindrome")