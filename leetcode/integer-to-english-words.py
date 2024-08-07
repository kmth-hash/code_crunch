# https://leetcode.com/problems/integer-to-english-words/description/

class Solution:

    unitsWords = {0 : 'Zero' , 1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
    tensWords = {20 : 'Twenty' , 30:'Thirty' ,40:'Forty' , 50:'Fifty' , 60:'Sixty' , 70:'Seventy' , 80:'Eighty' , 90:'Ninety'}
    teenWords = {10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}

    def findHundreds(self, num:int , suffix : str ='') :
        num = "{:03d}".format(num)
        h , t , u = int(num[0]) , int(num[1]) , int(num[2])
        res = ''
        if h!=0 : 
            res += f'{self.unitsWords[h]} Hundred '
        if t!=0 : 
            if t!=1 : 
                res += f'{self.tensWords[t*10]} '
                if u!=0 : 
                    res += f'{self.unitsWords[u]}'
            else : 
                res += f'{self.teenWords[t*10+u]}'
               
        else : 
            if u!=0 : 
                res += f'{self.unitsWords[u]}'
        if res!='':
            res = f'{res.strip()} {suffix}'
        return res
        
    def splitWords(self, num:int) : 
        ls = []
        # ln = len(str(num)) 
        i = 0 
        suffices = ['' , 'Thousand' , 'Million' , 'Billion']
        res = []
        if num<10 : 
            return self.unitsWords.get(num,'')
        while num : 
            # print(num%1000)
            ls.append(num%1000)
            num = num//1000
            i+=1
        for i,v in enumerate(ls) : 
            x=self.findHundreds(v , suffices[i])
            if x!='':
                res.append(x)
        # print(' '.join(res[::-1]),'------>')
        return ' '.join(res[::-1])
    
    def numberToWords(self, num: int) -> str:
        return self.splitWords(num).strip()
