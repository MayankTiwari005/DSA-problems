'''
target = 8
[2,4,1,6]
boolean output
'''
nums = [1,2,3,5,6,7,8,9,10]
def backtrack(index, total, subset, target) -> bool:
    if total == target:
        return True
    elif index>len(nums):
        return False
    if total>target:
        return False
    subset.append(nums[index])
    add = total + nums[index]
    pick = backtrack(index+1, add, subset, target)
    if pick == True:
        return True
    subset.pop()
    add = total
    not_pick = backtrack(index+1, add, subset, target)
    return not_pick



def without_subset(index, total, target):
    if total == target:
        return True
    elif index >= len(nums):
        return False
    elif total > target:
        return False
    add = total + nums[index]
    pick = without_subset(index+1, total, target)
    if pick == True:
        return True
    add = total
    not_pick = without_subset(index+1, total, target)
    return not_pick