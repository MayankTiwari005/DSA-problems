class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for ch in "balloon":
            freq[ch] = 0

        for ch in text:
            if ch in freq:
                freq[ch] += 1
        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )