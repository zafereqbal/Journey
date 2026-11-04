class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        # Sort the candidates to easily skip duplicates
        candidates.sort()
        
        def backtrack(start, current_target, path):
            # Base case: if target is met, add the path to results
            if current_target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Optimization: if the current element exceeds the target, stop exploring further
                if candidates[i] > current_target:
                    break
                
                # Skip duplicate elements at the same decision level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Include the candidate and move to the next index
                path.append(candidates[i])
                backtrack(i + 1, current_target - candidates[i], path)
                path.pop() # Backtrack
                
        backtrack(0, target, [])
        return res
