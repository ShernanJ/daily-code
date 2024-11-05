# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        count = 1
        comp = ""
        current = word[0]
        for i in range(1, len(word)):
            if word[i] == current and count < 9:
                count += 1
            else:
                comp += str(count) + current
                current = word[i]
                count = 1
        comp += str(count) + current
        return comp
                