def brute(nums, target):    # time = O(N), space = O(1)
    n = len(nums)
    first = -1
    last = -1
    for i in range(0,n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    if first == -1:
        return 0
    return (last - first) + 1
