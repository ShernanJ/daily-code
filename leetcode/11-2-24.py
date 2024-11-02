# Sliding Window / Hash Map

# Using 2 pointers to create a window
# Hash Map to keep track of characters and indices within current window
# Expand and contract the window by moving the right pointer

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] in index_map:
                left = max(left, index_map[s[right]] + 1)
            index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        return max_length