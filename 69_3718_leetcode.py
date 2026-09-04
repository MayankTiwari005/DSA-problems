
def brute(self, nums: list[int], k: int) -> int:
    n = len(nums)
    my_list = []
    while k not in nums:
        return k
    for i in range(0, n):
        if nums[i] % k == 0:
            my_list.append(nums[i])
    my_list.sort()
    for j in my_list:
        if j + k not in my_list:
            return j + k
    return k

def optimal(self, nums: list[int], k: int) -> int:
    nums_set = set(nums)
    curr = k
    while curr in nums_set:
        curr += k
    return curr