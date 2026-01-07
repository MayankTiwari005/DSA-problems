def InsertionSort(nums):
    n = len(nums)
    print(n)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key
    return nums

nums = [20,1,2,3,7,8,9,10]
print(InsertionSort(nums))


'''
def insertion(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j>=0 and j>key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key
    return nums
nums = [20,1,2,3,7,8,9,10]
print(insertion(nums))
'''