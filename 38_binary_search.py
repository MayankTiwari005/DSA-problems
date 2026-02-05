# BINARY SEARCH LEETCODE 704

def binary(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# USING RECURSION
def binary_search(nums, target, low, high):
    n = len(nums)
    while low < high:
        mid = (low + high) // 2
        if low > high:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(nums, target, mid+1, high)
        else:
            return binary_search(nums, target, low, mid-1)
