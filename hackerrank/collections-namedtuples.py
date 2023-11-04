#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
from collections import namedtuple
n = int(input())
column = list(map(str,input().split()))
Student = namedtuple('Student',column)
student = []
sum1 = 0
for i in range(n):
    a = input().split()
    student = Student(*a)
    sum1 = int(student.MARKS) + sum1
average = round(sum1 / n,2)
print(average)
