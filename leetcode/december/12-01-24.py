# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = []
        current = ""

        for c in sentence:
            if c != " ":
                current += c
            else:
                if current:
                    words.append(current)
                    current = ""
        if current:
            words.append(current)
        
        for i, word in enumerate(words):
            if len(word) >= len(searchWord):
                is_match = True
                for j in range(len(searchWord)):
                    if word[j] != searchWord[j]:
                        is_match = False
                        break
                if is_match:
                    return i + 1
        return -1