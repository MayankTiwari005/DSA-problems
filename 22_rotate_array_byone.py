def func(nums):
    n = len(nums)
    nums[:] = [nums[n-1]] + nums[0:n-1]
    return nums

nums = [5,4,8,7,9,1,0,3,1]
print(func(nums))


def rotate(arr):
    n = len(arr)
    temp = arr[n-1]
    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
    arr[0] = temp
    return arr

arr = [5,4,8,7,9,1,0,3,1]
k = int(input("enter k: "))
for _ in range(k):                  # BY K TERMS SHIFT BRUTE FORCE
    print(rotate(arr))
