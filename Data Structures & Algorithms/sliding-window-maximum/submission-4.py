from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []
        for i in range(k):
            heap.append((-nums[i], i))

        heapq.heapify(heap)

        result = [-(heap[0][0])]
        l = 0

        for r in range(k, n):
            l += 1
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            result.append(-heap[0][0])

        return result
