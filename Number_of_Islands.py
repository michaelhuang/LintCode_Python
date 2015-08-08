class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        count = 0
        self.grid = grid
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    self.dfs(i, j)
        return count

    # deep first search
    def dfs(self, i, j):
        # validity check
        if i < 0 or j < 0 or i >= len(self.grid) \
                or j >= len(self.grid[0]):
            return
        # cell is water or visited
        if self.grid[i][j] == 0:
            return
        # set visited
        self.grid[i][j] = 0
        # begin dfs
        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)
