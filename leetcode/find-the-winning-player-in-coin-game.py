# https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        x = min(x,y//4)
        if(x%2 == 0):
            return "Bob"
        return "Alice"
