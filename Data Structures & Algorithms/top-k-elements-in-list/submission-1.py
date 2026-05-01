import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []
        for val, freq in freq_map.most_common(k):
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]