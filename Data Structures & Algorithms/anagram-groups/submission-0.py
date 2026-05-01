from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        key_map = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                idx = ord(char) - ord("a")
                key[idx] += 1
            key = tuple(key)
            key_map[key].append(word)
        
        results = [ vals for vals in key_map.values()]
        return results
