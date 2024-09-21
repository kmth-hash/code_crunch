# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        self.ls = []

    def next(self, price: int) -> int:
        self.ls.append(price)
        ln = len(self.ls)
        for i in range(ln-2 , -1 , -1 ) : 
            if self.ls[i] > price : 
                return ln-i-1 
        return ln


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
