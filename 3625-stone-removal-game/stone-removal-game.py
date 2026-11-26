class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        remove = 10
        alice_turn = True
        
        while n >= remove and remove > 0:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn
            
        # If it is currently Alice's turn when the loop ends, she cannot move and loses
        return not alice_turn
