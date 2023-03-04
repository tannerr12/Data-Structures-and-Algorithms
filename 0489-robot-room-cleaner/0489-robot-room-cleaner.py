# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        #The tricky part with this question is not knowing where you are but the idea is to keep a virtual position grid and use it to mark a cell as seen
        #The other trick that I ran into issues with was the idea of going back where in normal dfs we can simply pop back to a previous state the robot must manually go back so after every successful move we go back
        #so that we can continue from that previous state
        directions = [[-1,0], [0,1], [1,0],[0,-1]]
        seen =set()
        d = 0
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def dfs(i,j):
            nonlocal d
            if (i,j) in seen:
                return
            seen.add((i,j))
            robot.clean()
            for val in range(4):
                if (i+directions[d][0], j + directions[d][1]) not in seen and robot.move():
                    dfs(i+directions[d][0], j + directions[d][1])
                    go_back()
                robot.turnRight()
                d+=1
                d %= 4
            

        dfs(0,0)
     