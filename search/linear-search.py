arr = [2,4,3,6,5,1,7]
target = 4


def linearSearch(arr , target):
    for i in range(0, len(arr)):
        if arr[i]==target : 
            return i
    return -1

res = linearSearch(arr , target) 
if res==-1 :
    print('Element not found ')
else : 
    print('Element found at index : ',res)
