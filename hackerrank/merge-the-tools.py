#https://www.hackerrank.com/challenges/merge-the-tools/problem
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    c = 0
    le_list = []
    ln = int(len(string)/k)
    #print(len(string))
    for i in range(ln) :
        le_list.append(string[i*k:(i+1)*k])
        c+=ln
    #print(le_list)
    for i in le_list:
        #print(i)
        print("".join(OrderedDict.fromkeys(i))  )

