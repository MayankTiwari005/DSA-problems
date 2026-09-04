nums = [5,3,9,4,1]
result = []

def brute(idx, target, subset):
    if idx>=len(nums):
        if sum == target:
            result.append(subset.copy())
        return
    subset.append(nums[idx])
    brute(idx+1, subset)
    subset.pop()
    brute(idx+1,subset)


answer = []
def optimal_func(index, target, total, subset):
    if total == target:
        answer.append(subset.copy())
        return
    elif index>=len(nums):
        return
    elif total > target:
        return
    subset.append(nums[index])
    get_sum = total + nums[index]
    optimal_func(index+1, target, get_sum, subset)
    e = subset.pop()
    get_sum = get_sum - e
    optimal_func(index+1, target, get_sum, subset)
