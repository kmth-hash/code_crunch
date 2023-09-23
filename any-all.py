#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
_, number_list = input(), input().split()
print(all([n > 0 for n in list(map(int, number_list))]) and any([n == n[::-1] for n in number_list]))