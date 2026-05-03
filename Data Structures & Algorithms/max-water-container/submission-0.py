class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_amount = 0

        left = 0
        right = n - 1

        while left < right:
            hl = heights[left]
            hr = heights[right]
            amount = min(hl, hr) * (right - left)
            max_amount = max(max_amount, amount)
            if hl < hr:
                left += 1
            else:
                right -= 1

        return max_amount
