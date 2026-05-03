class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        slow = 0
        seen = set()
        max_len = 0
        for fast in range(n):
            val = s[fast]
            while val in seen:
                lv = s[slow]
                seen.remove(lv)
                slow += 1
            seen.add(val)
            max_len = max(max_len, fast - slow + 1)

        return max_len
