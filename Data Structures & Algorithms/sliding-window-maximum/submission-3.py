from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []
        freq_map = {}
        for i in range(k):
            heap.append(-nums[i])
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

        heapq.heapify(heap)

        l = 0
        result = [-(heap[0])]

        for r in range(k, n):
            l_val = nums[l]
            r_val = nums[r]

            freq_map[l_val] -= 1
            l += 1
            freq_map[r_val] = freq_map.get(r_val, 0) + 1
            heapq.heappush(heap, -r_val)
            curr_max = -(heap[0])

            while freq_map[curr_max] <= 0:
                heapq.heappop(heap)
                curr_max = -(heap[0])

            result.append(curr_max)

        return result
