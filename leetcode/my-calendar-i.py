# https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.dates = []

    def book(self, start: int, end: int) -> bool:
        for i,j in self.dates : 
            if start>=j or end <= i : 
                pass 
            else : 
                return False 
        self.dates.append((start,end))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
