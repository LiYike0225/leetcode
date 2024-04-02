from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefixSum = defaultdict(int)
        n = len(wall)
        for i in range(0,n):
            curSum = 0
            for j in range(0, len(wall[i])-1):
                curSum += wall[i]
                prefixSum[curSum] += 1

        return n - max(prefixSum.values(), default =0)