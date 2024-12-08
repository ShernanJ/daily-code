# https://leetcode.com/problems/two-best-non-overlapping-events

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ans = most = 0 
        pq = []
        for st, et, val in sorted(events): 
            heappush(pq, (et, val))
            while pq and pq[0][0] < st: 
                _, vv = heappop(pq)
                most = max(most, vv)
            ans = max(ans, most + val)
        return ans 