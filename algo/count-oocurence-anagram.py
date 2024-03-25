from isAnagram import isAnagram


def countAnagram(text, word):
    # count = 0
    start = 0
    d = []

    for i in range(len(text)):

        if i-start+1 == len(word):
            if isAnagram(text[start: i+1], word):
                d.append(text[start: i+1])
            # subArr = text[start : ]
            start += 1

        print(start, i, text[start: i+1], d)

    # for i in range()
    return len(d)


def anagram_method(test, word):
    pass


text = 'gotxxotgxdogt'
word = 'got'


# print('Anagram',isAnagram('xxtg' , 'xtgg'))
res = countAnagram(text, word)


text = 'gttgfgthgftghh'
word = 'ght'

res = countAnagram(text , word) 