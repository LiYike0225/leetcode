class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res=s.split()
        return list(map(pattern.index, pattern)) == list(map(res.index, res))
