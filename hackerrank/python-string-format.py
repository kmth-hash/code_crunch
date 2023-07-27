#https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(n):
    space = len(bin(n)[2:])
    for i in range(1, n + 1):
        print(f'{i:>{space}} {oct(i)[2:]:>{space}} {hex(i)[2:].upper():>{space}} {bin(i)[2:]:>{space}}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)