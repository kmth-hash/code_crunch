arr = [7,-3,9,2,6,3,0]

for i in range(len(arr)) : 

    for j in range(0 , len(arr)-i-1) : 

        if arr[j] > arr[j+1] : 
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
        # print( i , j , arr)
print(arr)

