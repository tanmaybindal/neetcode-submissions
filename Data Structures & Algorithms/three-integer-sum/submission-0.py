class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        results = []
        for p1 in range(0, n - 2):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue

            p2 = p1 + 1
            p3 = n - 1

            while p2 < p3:
                curr_sum = nums[p1] + nums[p2] + nums[p3]

                if curr_sum > 0:
                    p3 -= 1
                elif curr_sum < 0:
                    p2 += 1
                else:
                    results.append([nums[p1], nums[p2], nums[p3]])
                    while p2 < p3 and nums[p2] == nums[p2 + 1]:
                        p2 += 1
                    while p2 < p3 and nums[p3] == nums[p3 - 1]:
                        p3 -= 1
                    
                    p2 += 1
                    p3 -= 1

        return results
                    
