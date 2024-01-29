# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ls = []
        for i in candies : 
            if i+extraCandies>=m :
                ls.append(True)
            else :
                ls.append(False)
        print(ls)
        return ls