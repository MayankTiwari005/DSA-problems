'''
subset occurances
'''

nums = [1,2,3]
result = []

def solve(idx, subset):
    if idx >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[idx])
    solve(idx+1,subset)
    subset.pop()
    solve(idx+1,subset)



