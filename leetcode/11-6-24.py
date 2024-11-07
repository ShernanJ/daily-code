# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
      
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1