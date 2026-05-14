class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            val = temperatures[i]
            while stack and val >= temperatures[stack[-1]]:
                stack.pop()

            results[i] = stack[-1] - i if len(stack) != 0 else 0
            stack.append(i)

        return results
