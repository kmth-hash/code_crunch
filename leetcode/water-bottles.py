# https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        tempRes = 0

        if numExchange > numBottles : 
            return numBottles 
        
        while numBottles>=numExchange :             
            tempRes = numBottles // numExchange 
            res += tempRes   
            numBottles = numBottles % numExchange + tempRes 
            
        return res
