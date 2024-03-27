def solution(arr , num ):
    print(arr , num)
    totalSum = 0
    left = 0
    right = 0
    minLen = 999999

    while left < len(arr) :

        if right < len(arr) and totalSum < num :
            print('adding : ', arr[right])
            totalSum += arr[right]
            right+= 1
        elif totalSum >= num :
            minLen = min(minLen , right-left)
            print('removing : ', arr[left])
            totalSum -= arr[left]
            left += 1

        else : 
            break

    if minLen == 999999:
        return 0
    else : 
        return minLen

print(solution([2,3,1,2,4,3], 7) )
print(solution([2,1,6,5,4], 9) )
print(solution([3,1,7,11,2,9,8,21,62,33,19], 52) )
print(solution([1,4,16,22,5,7,8,9,10], 39) )
print(solution([1,4,16,22,5,7,8,9,10], 55) )
print(solution([4,3,3,8,1,2,3], 11) )
print(solution([1,4,16,22,5,7,8,9,10], 95))