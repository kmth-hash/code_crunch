# https://leetcode.com/problems/lru-cache/description/

class LRUCache:

    def __init__(self, capacity: int):
        self.map = dict()
        self.ls = list()
        self.ln = 0 
        self.cap = capacity 

    def get(self, key: int) -> int:
        ret = self.map.get(key , -1) 
        if ret==-1 : 
            # print(self.map , self.ls , self.ln,'returning -->',ret)
            return ret 
        else :
            self.ls.remove(key)
            # print(f'{key} removed in {self.ls}') 
            self.ls.append(key)
            # print(self.map , self.ls , self.ln,'returning -->',ret)
            return ret

    def put(self, key: int, value: int) -> None:
        # print('adding : ',key)
        if key in self.map : 
            self.map[key] = value 
            self.ls.remove(key)
            self.ls.append(key)
        else : 
            self.ln += 1 
            self.map[key] = value 
            self.ls.append(key)
        
        if self.ln==self.cap+1 : 
            k = self.ls.pop(0)
            del self.map[k]
            self.ln=self.cap
        # print(self.map , self.ls , self.ln)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
