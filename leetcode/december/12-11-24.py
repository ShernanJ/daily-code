# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        for num in nums:
            if num - nums[l] > 2*k:
                l += 1
        return len(nums) - l