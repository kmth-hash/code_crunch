# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x , y = 0 , 0 
        obstacles = set((x, y) for x, y in obstacles)
        dir = 0 
        res = 0

        for i in commands : 
            if i==-1 : 
                dir = (dir+1)%4
                # print(d2[dir])
            elif i==-2 : 
                dir = (dir-1)%4
                # print(d2[dir])
            else : 
                if dir==0 : 
                    for j in range(1,i+1) : 
                        if (x,y+1) not in obstacles :
                            # print('Checking : ',x,y, 1+y) 
                            y = y+1
                            # max_y = max(abs(y) , max_y)
                        else : 
                            # print('Obstacle found : ')
                            break 
                elif dir==1 : 
                    for j in range(1,i+1) : 
                        if (x+1,y) not in obstacles :
                            # print('Checking : ',x,y,x+1) 
                            x = x + 1
                            # max_x = max(abs(x) , max_x)
                        else : 
                            # print('Obstacle found : ')
                            break 
                elif dir==2 : 
                    for j in range(1,i+1) : 
                        if (x,y-1) not in obstacles :
                            # print('Checking : ',x,y,y-1) 
                            y = y-1
                            # max_y = max(abs(y) , max_y)
                        else : 
                            # print('Obstacle found : ')
                            break 
                elif dir==3 : 
                    for j in range(1,i+1) : 
                        if (x-1,y) not in obstacles :
                            # print('Checking : ',x,y,x-1) 
                            x -= 1
                            # max_x = max(abs(x) , max_x)
                        else : 
                            # print('Obstacle found : ')
                            break 


            res = max(x*x+y*y, res)
        return res
