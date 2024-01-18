# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = len(searchWord)
        c = 1
        for i in sentence.split(' '):
            # print(i[:l])
            if i[:l]==searchWord:
                print('found')
                return c
            c += 1
        return -1