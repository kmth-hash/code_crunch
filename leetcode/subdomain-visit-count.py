# https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = Counter()
        for v in cpdomains : 
            num , domains = v.split(' ')
            ls = list(domains.split('.'))
            for i in range(len(ls)) : 
                key = '.'.join(ls[i:])
                if key not in c : 
                    c[key] = int(num)
                else : 
                    c[key] += int(num)
            
        res = []
        for citr in c : 
            res.append(f'{c[citr]} {citr}')
        return res
