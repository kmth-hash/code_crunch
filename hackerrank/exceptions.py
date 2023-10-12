
# https://www.hackerrank.com/challenges/exceptions/problem
n = int(input())
for i in range(n):
    m  = list(map(str , input().rstrip().split()))
    try : 
        res = int(m[0])//int(m[1])
        print(res)
    except ZeroDivisionError as e:
        
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: invalid literal for int() with base 10: '{m[1] if m[0].isdigit() else m[0]}'")
    
