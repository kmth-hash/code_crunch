# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        temp_sum = skill[0]+skill[-1]
        chemsum = 0 
        ln = len(skill)
        for i in range(ln//2) :  
            if skill[i]+skill[-1-i] != temp_sum : 
                return -1 
            chemsum += (skill[i] * skill[-1-i])
        return chemsum
