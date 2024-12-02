# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        num_cols = len(matrix[0])
        max_rows = 0

        for current_row in matrix:
            flipped_row = [1 - x for x in current_row]

            row_count = sum(
                1
                for compare_row in matrix
                if compare_row == current_row or compare_row == flipped_row
            )

            max_rows = max(max_rows, row_count)
        return max_rows