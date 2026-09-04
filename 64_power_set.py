'''
leetcode 78
all subset occurances
'''

def bit_manipulation(array):
    n = len(array)
    total_subset = 1<<n
    result = []
    for num in range(0,total_subset):
        lst = []
        for i in range(0,n):
            if num&(1<<i)!=0:
                lst.append(num[i])
        result.append(lst)
    return result