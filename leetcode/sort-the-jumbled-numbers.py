# https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-08-07

class Solution:
    mainMapping = []
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        self.mainMapping = []
        
        for i in nums : 
            self.mainMapping.append( (i , self.findNewValue(mapping , i)    ))
        x = self.mainMapping
        x.sort(key=lambda x : x[1])
        # print(x)
        return [r for r,s in x]
    def findNewValue(self , mapping , curr) : 
        newKey = ''.join([str(mapping[int(i)]) for i in str(curr)])
        return int(newKey)

