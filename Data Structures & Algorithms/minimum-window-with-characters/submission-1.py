from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if m > n:
            return ""

        freq_map = defaultdict(int)

        l = 0
        r = 0
        min_len = float("inf")

        remaining = 0
        start_idx = 0

        for ch in t:
            freq_map[ch] += 1
            remaining += 1

        while r < n:
            val = s[r]
            if freq_map[val] > 0:
                remaining -= 1
            freq_map[val] -= 1

            while remaining == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start_idx = l
                l_val = s[l]
                freq_map[l_val] += 1
                if freq_map[l_val] > 0:
                    remaining += 1
                l += 1
            r += 1

        if min_len == float("inf"):
            return ""
        return s[start_idx : start_idx + min_len]
