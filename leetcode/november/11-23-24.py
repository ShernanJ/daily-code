# https://leetcode.com/problems/maximum-matrix-sum

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_val = float("inf")
        count = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    count += 1
                min_val = min(min_val, abs(val))
        
        if count % 2 != 0:
            total -= 2 * min_val

        return total