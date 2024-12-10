"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if all(cell == grid[0][0] for row in grid for cell in row):
            return Node(bool(grid[0][0]), True)
        
        # if not, return a node with all smaller grids
        n = len(grid) // 2
        return Node(True, False, self.construct([row[:n] for row in grid[:n]]),
                                 self.construct([row[n:] for row in grid[:n]]),
                                 self.construct([row[:n] for row in grid[n:]]),
                                 self.construct([row[n:] for row in grid[n:]]))