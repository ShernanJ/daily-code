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
      
      
# https://leetcode.com/problems/circular-sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        
        for i in range(len(words)):
            current_word = words[i]
            next_word = words[(i + 1) % len(words)]
            
            if current_word[-1] != next_word[0]:
                return False
                
        return True
      
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and (sentence[i-1] != sentence[i+1]):
                return False
        return sentence[0] == sentence[-1]