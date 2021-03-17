class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        answer = []

        def dfs(letters: str, idx: int):
            if len(letters) == len(digits):
                answer.append(letters)
                return

            for i in range(idx, len(digits)):
                for j in dic[digits[i]]:
                    dfs(letters + j, i + 1)

        if not digits:
            return []

        dfs('', 0)

        return answer