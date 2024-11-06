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
                
                
# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write in the chars array
        count = 1  # Counter for occurrences of each character
        
        for read in range(1, len(chars) + 1):
            # If we reach the end of the array or encounter a new character
            if read == len(chars) or chars[read] != chars[read - 1]:
                # Write the character
                chars[write] = chars[read - 1]
                write += 1
                
                # Write the count if greater than 1
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                
                # Reset count for the new character
                count = 1
            else:
                # Increment the count for consecutive characters
                count += 1
        
        return write