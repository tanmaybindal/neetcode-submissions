class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums: number[]): number[] {
        const len = nums.length;
        const ans = [];

        for (let i = 0; i < len; i++) {
            ans[i] = nums[i]
            ans[i+len] = nums[i]
        }

        return ans;
    }
}
