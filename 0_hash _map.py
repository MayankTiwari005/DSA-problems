# storing number of occurances
from collections import defaultdict
def func(nums):
    n = len(nums)
    visited = [False]*n
    for i in range(0,n):
        if visited[i]:
            continue

        count = 1
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                visited[j] = True
                count += 1
        print(nums[i], count)


def optimal(arr):
    n = len(arr)
    freq_map = {}
    for i in range(0,n):
        if arr[i] in freq_map:
            freq_map[arr[i]] += 1
        else:
            freq_map[arr[i]] = 1
    for key, value in freq_map:
        return key,value



def lib(num):
    n = len(num)
    freq_map = defaultdict(int)

    for i in range(0,n):
        freq_map[num[i]] += 1
    for key, value in freq_map.items():
        return key,value