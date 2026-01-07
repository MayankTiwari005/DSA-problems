# LEETCODE 189

#   BRUTE FORCE
def rotate(nums, k: int) -> None:
    n = len(nums)
    rotational  = k%n
    for _ in range(0,rotational):
        e = nums.pop()
        nums.insert(0,e)

#   BETTER SOLUTION
#   USING SLICING (python special)

def slice(arr, k: int) -> None:
    n = len(arr)
    k = k%n
    arr[:] = arr[n-k:] + arr[:n-k]

#  OPTIMAL SOLUTION, OTHER THAN PYTHON LANGUAGES

def rotate(self, nums, k: int) -> None:
    n = len(nums)
    k = k%n
    def rev(arr, left, right):
        while arr [left] < arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right += 1
    rev(nums, n-k, n-1)
    rev(nums, 0, n-k-1)
    rev(nums, 0, n-1)