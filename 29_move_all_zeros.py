# leetcode 283
'''
Docstring for DSA.29_move_all_zeros
nums = [0,1,0,3,2,4]
ident 1: i = 0, nothing to do   
ident 2: i=1 and j+=1, swap i,j -> [1, 0 -> j, 0, 3, 2, 4]

'''
def func(nums):
    n = len(nums)
    j = 0
    for i in range(0,n):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j
