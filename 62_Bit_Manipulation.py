
'''
integer 9 has bit as 1001
same as integer 13 has bit as 1101
'''

# complexity both: O(log base2 n)

def convert_int_to_binary(num:int) -> str :
    results = ""
    while num>0:
        if num%2 == 1:
            result += "1"
        else:
            result += "0"
        num = num//2
    
    result = results[::-1]
    return result

def convert_to_int(x:str) -> int:
    decimal_num = 0
    power = 0
    index = len(x) - 1
    while index >=0:
        num = int(x[index]) * (2**power)
        decimal_num += num

        index -= 1
        power += 1

    return decimal_num