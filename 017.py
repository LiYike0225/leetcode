class Solution:
    def lettercombinations(self, digits: str) -> list[str]:
        phoneMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                combinations.append(curStr)
                return

            for c in phoneMap[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return combinations

print(Solution().lettercombinations("23"))

