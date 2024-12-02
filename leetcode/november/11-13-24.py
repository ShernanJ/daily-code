# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        while l < r:
            mid = (l + r) // 2
            
            if (sum((quantity + mid - 1) // mid for quantity in quantities) <= n):
                r = mid
            else:
                l = mid + 1

        return l