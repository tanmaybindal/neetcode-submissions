class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prefix = [1] * n

        for i in range(1, n):
            left_prefix[i] = nums[i - 1] * left_prefix[i - 1]

        right_prefix = [1] * n

        for i in range(n - 2, -1, -1):
            right_prefix[i] = nums[i + 1] * right_prefix[i + 1]

        result = []

        for i in range(n):
            result.append(left_prefix[i] * right_prefix[i])

        return result
