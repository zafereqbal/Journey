class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Array to store net trust scores for people labeled 1 to n
        trust_scores = [0] * (n + 1)
        
        # Calculate net score for each trust relationship
        for a, b in trust:
            trust_scores[a] -= 1  # Person 'a' trusts someone, decrease score
            trust_scores[b] += 1  # Person 'b' is trusted, increase score
            
        # Check who has a score equal to n - 1
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1
