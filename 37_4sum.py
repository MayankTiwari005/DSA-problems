# leetcode 18

def brute(nums, target):
    n = len(nums)
    if n < 4:
        return nums
    my_set = set()
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    
    result = []
    #return (list[ans] for ans in my_set)
    for ans in my_set:
        result.append(list(ans))
    return result


# fourth = target - (nums[i] + nums[j] + nums[k])
# hash_set will recoganise if element is there or not

def better(nums, target):
    n = len(nums)
    if n < 4:
        return nums
    my_set = set()
    for i in range(0,n):
        for j in range(i+1, n):
            hash_set = set()
            for k in range(j+1, n):
                fourth = target - (nums[i] + nums[j] + nums[k])
                if fourth in hash_set:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    my_set.add(tuple(temp))
                hash_set.add(nums[k])
    
    result = []
    for ans in my_set:
        result.append(list(ans))
    return result


def optimal(nums, target):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(0,n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                            # rest code will not run and i increments
        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n -1

            while j < k:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                    
                elif total < target:
                    k += 1
                else:
                    l -= 1
    
    return ans