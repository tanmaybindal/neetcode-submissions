from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_prefix = [0] * n

        for i in range(1, n):
            left_prefix[i] = max(height[i - 1], left_prefix[i - 1])

        right_prefix = [0] * n

        for i in range(n - 2, -1, -1):
            right_prefix[i] = max(right_prefix[i + 1], height[i + 1])

        amount = 0

        for i in range(n):
            amount += max(min(left_prefix[i], right_prefix[i]) - height[i], 0)

        return amount
