class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        freq = [0] * 26
        l = 0
        for ch in s1:
            idx = ord(ch) - ord("a")
            freq[idx] += 1

        key = tuple(freq)

        freq = [0] * 26

        for r in range(m):
            ch = s2[r]
            idx = ord(ch) - ord("a")
            freq[idx] += 1

            if r - l + 1 > n:
                lch = s2[l]
                l_idx = ord(lch) - ord("a")
                freq[l_idx] -= 1
                l += 1
            
            if(key == tuple(freq)):
                return True
        
        return False

