

def largestSum(arr , k):
    totalSum = 0
    tempSum = 0
    start = 0
    
    for i in range(len(arr)):
        tempSum += arr[i]
        
        # print( i , totalSum , tempSum , start)
        if(i-start+1)==k:
            totalSum  = max(totalSum , tempSum)
            tempSum -= arr[start]            
            start += 1 
        # print( start, i , totalSum , tempSum  )
    return totalSum


arr = [ 5, 7, 1, 4, 3, 6, 2, 9, 2 ]
k=5

x = largestSum(arr, k)
print('Result : ' , x)

arr = [3, 5, 2, 1, 7]
k=2

x = largestSum(arr, k)
print('Result : ' , x)
