# Selection sort 
# Select minimum most element in array at each iteration 
# Place it in i-th index 

A  = [64, 25, 12, 22, 11] 

for i in range(len(A)):
    min_itr = i

    for j in range(i+1 , len(A)):
        if A[min_itr] > A[j] : 
            min_itr = j 
    
    A[i] , A[min_itr] = A[min_itr] , A[i] 

print(A)
