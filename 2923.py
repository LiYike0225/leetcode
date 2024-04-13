class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        n = len(grid)
        for i, line in enumerate(grid):
            if sum(line) == n - 1:
                return i


