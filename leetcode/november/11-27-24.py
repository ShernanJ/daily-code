# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        answer = []
        n = len(s)
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            i = curr_row
            while i < n:
                answer.append(s[i])
            
                if curr_row != 0 and curr_row != numRows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    j = i + chars_in_between

                    if j < n:
                        answer.append(s[j])
                    
                i += chars_in_section
            
        return "".join(answer)
