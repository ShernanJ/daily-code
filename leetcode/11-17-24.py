# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")

        curr = 0
        q = deque()

        for i in range(len(nums)):
            curr += nums[i]
            
            if curr >= k:
                res = min(res, i + 1)
        
            while q and curr - q[0][0] >= k:
                prefix, end = q.popleft()
                res = min(res, i - end)
            
            while q and q[-1][0] > curr:
                q.pop()
            q.append((curr, i))

        return -1 if res == float("inf") else res