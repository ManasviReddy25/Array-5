# Problem1: Bind Robot in a Circle (https://leetcode.com/problems/robot-bounded-in-circle/)
# Time Complexity: O(n), n = length of instructions (one pass)
# Space Complexity: O(1), only a few variables
# Approach:
# Run the instructions once, starting at (0, 0) facing north.
# After one round, if the robot is back at the origin, it repeats the same path forever, so it is bounded.
# If it is not at the origin but faces a new direction, its path keeps turning and returns to the origin within 4 rounds, so it is bounded.
# If it is not at the origin and still faces north, it drifts away forever, so it is not bounded.
# Return True if (at origin) or (not facing north).

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # [dx, dy] for North, West, South, East (left-turn order)
        dirs = [[0,1],[-1,0],[0,-1],[1,0]]
        # start at origin, index 0 = facing North
        x,y,index = 0,0,0

        # run the instructions once
        for c in instructions:
            # move one step in the current direction
            if c == "G":
                x += dirs[index][0]  # change x by dx
                y += dirs[index][1]  # change y by dy
            # turn left: next direction in the list, wrap with % 4
            if c == "L":
                index = (index + 1)%4
            
            # turn right: one step back in the list (+3 avoids negatives)
            if c == "R":
                index = (index + 3)%4
        # bounded if back at origin OR not facing north
        return (x==0 and y==0) or index !=0
