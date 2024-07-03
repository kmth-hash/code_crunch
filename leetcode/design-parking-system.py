# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkSize = [big , medium ,small]
        self.carz = [0,0,0]

    def addCar(self, carType: int) -> bool:
        if carType==1 :
            if self.carz[0]+1>self.parkSize[0]:
                return False
            else : 
                self.carz[0] += 1
                return True
            
        if carType==2 :
            if self.carz[1]+1>self.parkSize[1]:
                return False
            else : 
                self.carz[1] += 1
                return True

        if carType==3 :
            if self.carz[2]+1>self.parkSize[2]:
                return False
            else : 
                self.carz[2] += 1
                return True
            
            


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
