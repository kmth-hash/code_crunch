#pending
def fun(s):
    flag = True
    if not '@' in s or (s.count('@')>1):
        # print('@')
        return False 
    if not '.' in s or (s.count('.')>1):
        # print('.')
        return False
    u = s.split('@')[0]
    w = (s.split('@')[1]).split('.')[0]
    e = (s.split('@')[1]).split('.')[1]
    # print(u,w,e)
    
    for i in u:
        if i.isalpha() or i.isdigit() or i=='-' or i=='_':
            # print(i)
            flag = True
        else:
            # print('1')
            flag = False 
    for i in e:
        if not i.isalpha():
            # print('2')
            flag = False 
    if len(e)>3:
        # print('3')
        flag = False
    # print(s,flag)
    return flag
    
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)