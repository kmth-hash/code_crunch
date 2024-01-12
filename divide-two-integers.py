# https://leetcode.com/problems/divide-two-integers/description/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        neg=( (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0) )
        print(neg)
        x, y = abs(dividend), abs(divisor)
        print(x,y)
        zgen=range(y,x,y)
        zlen=len(zgen)
        print(zgen , zlen)
        if y > x:
            return 0
        if x == y:
            return -1 if neg else 1
        
        if zgen[-1] + y <= x:
            zlen+=1

        if neg:
            return 0 - zlen
        return min(max(-2147483648,zlen),2147483647)