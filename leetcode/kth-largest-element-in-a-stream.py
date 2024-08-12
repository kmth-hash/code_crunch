# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/?envType=daily-question&envId=2024-08-12

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        # print(self.nums)
        
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        # print(self.nums)
        self.nums = sorted(self.nums, reverse=True)
        # print(self.nums , self.nums[self.k-1])
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
