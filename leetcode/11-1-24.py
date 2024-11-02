# https://leetcode.com/problems/delete-characters-to-make-fancy-string

class Solution:
    def makeFancyString(self, s: str) -> str:
        output = []

        if len(s) < 3:
            return s

        for char in s:
            if len(output) < 2 or not (output[-1] == output[-2] == char):
                output.append(char)
        return ''.join(output)