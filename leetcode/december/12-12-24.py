# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        seconds = k
        current_second = 0

        while current_second < seconds:
            
            gifts = sorted(gifts)
            gifts[-1] = math.floor(math.sqrt(gifts[-1]))

            current_second += 1
        
        answer = 0

        for i in gifts:
            answer += i

        return answer

# [25, 64, 9, 4, 100] 0
# [25, 64, 9, 4, 10]  1
# [25, 8, 9, 4, 10]   2
# [5, 8, 9, 4, 10]    3
# [5, 8, 9, 4, 3]     4