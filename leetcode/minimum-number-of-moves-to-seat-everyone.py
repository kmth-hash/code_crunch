# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/?envType=daily-question&envId=2024-06-13

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)) : 
            res += abs(seats[i]-students[i])
        return res
