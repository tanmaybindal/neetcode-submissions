class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = [(temperatures[-1], n - 1)]
        # 1,2,3,4,5
        for i in range(n - 2, -1, -1):
            val = temperatures[i]
            while stack and val >= stack[-1][0]:
                stack.pop()

            results[i] = stack[-1][1] - i  if len(stack) != 0 else 0
            stack.append((val, i))
        
        return results
