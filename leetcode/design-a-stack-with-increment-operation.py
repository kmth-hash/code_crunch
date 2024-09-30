# https://leetcode.com/problems/design-a-stack-with-increment-operation/description/?envType=daily-question&envId=2024-09-30

class CustomStack:

    def __init__(self, maxSize: int):
        self.ls = []
        self.stMax = maxSize
        self.ln = 0
          
    def push(self, x: int) -> None:
        if self.ln<self.stMax : 
            self.ls.append(x)
            self.ln += 1
    def pop(self) -> int:
        if self.ls : 
            self.ln -= 1 
            return self.ls.pop(-1)
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k) : 
            if self.ls and self.ln>i : 
                self.ls[i]+= val
            else : 
                break
        # print(self.ls)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
