def brute(nums, target):
    n = len(nums)
    first = -1
    last = - 1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]

def optimal(nums, target):
    def lower_bound(nums, taget):
        n = len(nums)
        lb = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = nums[mid]
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def upper_bound(nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ub = -1
        while low <= high:
            if nusm[mid] <= target:
                up = nums[mid]
                low = mid + 1
            else:
                high = high - 1
        return ub
    return ub - lb