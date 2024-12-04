# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index, length = 0, len(str2)
        for current in str1:
            if index < length and (ord(str2[index]) - ord(current)) % 26 < 2:
                index += 1
        return index == length