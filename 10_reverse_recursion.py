def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left+1, right-1)

arr = [0,1,5,7,9,3,4,6,25,20]

func(arr, 0, 9)
print(arr)



# USING WHILE LOOP

nums = [0,10,20,30,40]
l=0
r=len(nums)-1
while l<r:
    nums[l], nums[r] = nums[r], nums[l]
    l+=1
    r-=1
print(nums)