#Difference between maximum and minimum average continuous k-length sub arrays 
#   
# from math import avg

def minmaxavg(arr , k):
    start = 0
    minAvg = sum(arr[:k])/k
    maxAvg = sum(arr[:k])/k
    # print(arr[:k] , minAvg , maxAvg)

    for i in  range(len(arr)):
        

        if i-start+1 ==k : 
            tempArr = sum(arr[start : start+k])
            minAvg = min( minAvg , tempArr/k)
            maxAvg = max( maxAvg , tempArr/k)
            start += 1
            # print(minAvg , maxAvg  , tempArr , i)
    

    print('Result --> ' ,maxAvg - minAvg)

arr = 3, 8, 9, 15
k = 2
minmaxavg(arr , k)