class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const s = new Set(nums)
        return s.size !== nums.length 
    }
}
