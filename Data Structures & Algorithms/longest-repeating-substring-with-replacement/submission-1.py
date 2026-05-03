class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        res = 0

        l = 0
        max_freq = 0

        for r in range(n):
            val = s[r]
            count[val] = count.get(val, 0) + 1
            max_freq = max(max_freq, count[val])

            if (r - l + 1) - max_freq > k:
                l_val = s[l]
                count[l_val] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res