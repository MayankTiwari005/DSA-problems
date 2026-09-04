

def optimal(self, n) -> bool:
    temp = n
    add = 0
    product = 1
    
    while temp>0:
        last_digit = temp%10
        add += last_digit
        product = product*last_digit
        temp = temp//10

    if n%(add+product) == 0:
        return True
    else:
        return False
    