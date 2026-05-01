from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        results = []
        for val, _ in freq_map.most_common(k):
            results.append(val)

        return results