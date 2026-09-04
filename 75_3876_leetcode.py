# PARITY ARRAY

def paritry_check(self, nums) -> bool:
    mini = min(nums)
    if mini%2==1:
        return True
    for i in nums:
        if i%2==1:
            return False
    return True