class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visit=set()
        maxarea=0

        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in visit:
                return 0
            
            visit.add((r,c))

            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            area=1
            for dr,dc in directions:
                area+=dfs(dr+r, c+dc)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxarea=max(maxarea,dfs(r,c))
        return maxarea
                    
                

            

        