class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # i instead of i + 1 because
                # the same number can be reused
                backtrack(i, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)

        return result