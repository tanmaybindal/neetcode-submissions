class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        slow = 0
        seen = {}
        max_len = 0
        for fast in range(n):
            val = s[fast]
            if val in seen:
                slow = max(seen[val] + 1, slow)
            seen[val] = fast
            max_len = max(max_len, fast - slow + 1)

        return max_len
