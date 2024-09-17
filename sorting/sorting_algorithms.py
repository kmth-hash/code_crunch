class Solution : 
    def selection_sort(self , ls) : 
        for i in range(len(ls)) : 
            minInd = i 
            for j in range(i, len(ls)) : 
                if ls[minInd] > ls[j] : 
                    minInd = j 
            ls[i],ls[minInd] = ls[minInd],ls[i]
        return ls



inputTestCases = [
    [2,3,5,1,4,8,7] , 
    [1,2,3,4,5,6,7] , 
    [] , 
    [0,0,0,0,0],
    [9,8,7,6,5,4,3,2,1,0],
    [4,6,87,3,7,3,7,7,89,3,1]
]


obj = Solution()
for eachTC in inputTestCases : 
    print(f'Testcase : {eachTC}')
    res = obj.selection_sort(eachTC)
    print('Selection sort : ',res)
    
    
