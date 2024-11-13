# https://leetcode.com/problems/count-the-number-of-fair-pairs

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.countLess(nums, upper) - self.countLess(nums, lower - 1)

    def countLess(self, nums: list[int], target_sum: int) -> int:
        res = 0
        i, j = 0, len(nums) - 1
        
        while i < j:
            while i < j and nums[i] + nums[j] > target_sum:
                j -= 1
            res += j - i
            i += 1
        
        return res