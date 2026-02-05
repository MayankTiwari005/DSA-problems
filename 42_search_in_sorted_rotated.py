def brute(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == n:
            return i

    return -1

def optimal(nums, target):
    n = len(nums)
    
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + mid)//2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[mid] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1
    