
def largestAltitude(self, gain: list[int]) -> int:
    res = [0,]
    i = 0
    n = len(gain)
    while i < n:
        res.append(res[i] + gain[i])
        i = i+1
    return max(res)
