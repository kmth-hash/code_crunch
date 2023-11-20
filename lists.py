#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    lst = []
   
    for _ in range(N): 
        user_input = input()
        command = user_input.split(" ")[0]
        
        if command == "insert":
            i = int(user_input.split(" ")[1])
            e = int(user_input.split(" ")[2])
            lst.insert(i, e)
        elif command == "print":
            print(lst)
        elif command == "remove":
            e = int(user_input.split(" ")[1])
            lst.remove(e)
        elif command == "append":
            e = int(user_input.split(" ")[1])
            lst.append(e)
        elif command == "sort":
            lst.sort()
        elif command== "pop":
            lst.pop()
        elif command == "reverse":
            lst.reverse()