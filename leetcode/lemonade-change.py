# https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = []
        def addCoins(ls) : 
            nonlocal counter
            for i in ls : 
                counter.append(i)
        def removeCoins(ls) : 
            nonlocal counter
            for i in ls : 
                counter.remove(i)
        

        for bill in bills : 
            if bill==5 : 
                addCoins([5])
            elif bill==10 and 5 in counter : 
                addCoins([10])
                removeCoins([5])
                # print(counter)
            elif bill==10 and 5 not in counter : 
                # print('10 false')
                return False 

            elif bill==20 : 
                if 10 in counter and 5 in counter : 
                    addCoins([20])
                    removeCoins([5,10])
                elif counter.count(5)>=3 : 
                    removeCoins([5,5,5])
                    addCoins([20])
                else : 
                    print('20 false ')
                    return False 
            # print(bill , counter)
        return True
