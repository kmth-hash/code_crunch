class Solution : 
    def selection_sort(self , ls) : 
        for i in range(len(ls)) : 
            minInd = i 
            for j in range(i, len(ls)) : 
                if ls[minInd] > ls[j] : 
                    minInd = j 
            ls[i],ls[minInd] = ls[minInd],ls[i]
        return ls

    def bubble_sort(self,ls) : 
        ln = len(ls)
        for i in range(ln) : 
            flag = False
            for j in range(1,ln) : 
                if ls[j]<ls[j-1] :  
                    ls[j-1],ls[j]=ls[j],ls[j-1]
                    flag = True 
            if not flag : 
                break
            # print(ls)
        return ls      
    def insertion_sort(self,ls) : 
        for i in range(1, len(ls)):
            key = ls[i]
            j = i - 1

            while j >= 0 and key < ls[j]:
                ls[j + 1] = ls[j]
                j -= 1
            ls[j + 1] = key
            # print(ls)
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
    # res = obj.selection_sort(eachTC)
    # print('Selection sort : ',res)
    res = obj.bubble_sort(eachTC)
    print('Bubble Sort : ',res)
    # break
    
