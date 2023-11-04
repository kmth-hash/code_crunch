#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ls = list(set(arr))
    ls.sort()
    # print(ls)
    print(ls[-2])
