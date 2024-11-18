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

# https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        
        if k == 0:
            return result
        
        for i in range(len(result)):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    result[i] += code[j % len(code)]
            else:
                for j in range(i - abs(k), i):
                    result[i] += code[(j + len(code)) % len(code)]
        return result