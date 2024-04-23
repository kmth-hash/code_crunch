# https://leetcode.com/problems/number-of-recent-calls/description


class RecentCounter:

    def __init__(self):
        self.res = []

    def ping(self, t: int) -> int:
        self.res.append(t)
        # print([i for i in self.res if t-i<=3000])
        return sum([1 for i in self.res if t-i<=3000])



# Solution #2
# class RecentCounter:

#     def __init__(self):
#         self.res = deque()

#     def ping(self, t: int) -> int:
#         self.res.append(t)
#         while self.res[0]<t-3000 : 
#             self.res.popleft()
#             # print(self.res)
#         return len(self.res)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
