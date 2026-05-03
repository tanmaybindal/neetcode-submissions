class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const n = s.length;
        let l = 0;

        const freqMap = {};
        let maxFreq = 0;
        let res = 0;
        for (let r = 0; r < n; r++) {
            const val = s[r];
            freqMap[val] = (freqMap[val] || 0) + 1;
            maxFreq = Math.max(maxFreq, freqMap[val]);

            if (r - l + 1 - maxFreq > k) {
                const val = s[l];
                freqMap[val] -= 1;
                l++;
            }

            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
