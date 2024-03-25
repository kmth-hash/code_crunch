def isAnagram(str1 , str2):
    if len(str1)!=len(str2):
        return False 
    if str1==str2:
        return True 
    d = [0] * 26

    for i in str1:
        d[ord( i)-ord('a')] += 1

    for i in str2:
        d[ord(i) -ord('a') ] -= 1

    for i in d :
        if i!=0 : 
            return False 
    return True



# print(isAnagram('got' , 'tgo'))
# print(isAnagram('gg' , 'ggg'))
# print(isAnagram('skyline' , 'skiline'))
# print(isAnagram('ggxgtg' , 'gggxgt'))
# print(isAnagram('got' , 'got'))
# print(isAnagram('xxtg' , 'xtgg'))


