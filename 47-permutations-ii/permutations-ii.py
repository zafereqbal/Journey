class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Step 1: Sort to place duplicates adjacent to each other
        visited = [False] * len(nums)
        
        def backtrack(path):
            # Base case: if the path length equals nums length, a valid permutation is formed
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # If already used in the current path, skip it
                if visited[i]:
                    continue
                
                # Step 3: Skip duplicates to ensure unique combinations
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                # Mark as visited and choose the number
                visited[i] = True
                path.append(nums[i])
                
                # Recurse
                backtrack(path)
                
                # Undo the choice (backtrack)
                path.pop()
                visited[i] = False
                
        backtrack([])
        return res
