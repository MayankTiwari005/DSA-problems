#   BRUTE FORCE

def brute(arr):
    arr.sort()
    return arr[-2]       #  OR return arr(n-2)

print(brute([3, 5, 1, 4]))

#   BETTER APPROACH

def func(nums):
    n = len(nums)
    largest = float("-inf")
    second_largest = float("-inf")

    for i in range(0, n):
        largest = max(largest, nums[i])

    for i in range(0,n):
        if nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]
    
    return largest, second_largest

print(func([3, 5, 1, 4]))


#   OPTIMAL APPROACH

def optimal(num):
    n = len(num)
    largest_num = float("-inf")
    second_largest_num = float("-inf")
    for i in range(0, n):
        if num[i] > largest_num:
            second_largest_num = largest_num     # store -inf value of largest_num in iteration 1
            largest_num = num[i]                 # -inf to 55 in iteration 1
        elif num[i] > second_largest_num and num[i] != largest_num:
            second_largest_num = num[i]
    
    return second_largest_num

print(optimal([3, 5, 1, 4]))
