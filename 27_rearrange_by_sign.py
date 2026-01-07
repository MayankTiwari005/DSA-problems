# leetcode 2149

def func(nums):
    n = len(nums)
    pos = []
    neg = []
    for i in range (0,n):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    print(pos)
    print(neg)
    for j in range(len(nums)):
        nums[2*j] = pos[j]
        nums[(2*j)+1] = neg[j]
    return nums

def optimal(nums):
    n = len(nums)
    result = [0]*n
    pos_index = 0
    neg_index = 1
    for i in range(0,n):
        if nums[i] >= 0:
            result[pos_index] = nums[i]
            pos_index +=2
        else:
            result[neg_index] = nums[i]
            neg_index += 2
    return result