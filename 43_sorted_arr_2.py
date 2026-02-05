# leetcode 81
# nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]
# nums = [10,11,11,12,12,13,13,13,1,2,3,4]

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
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        
        if nums[mid] == nums[low] == nums[high]:
            low += 1
            high -= 1
            continue
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1
    return False