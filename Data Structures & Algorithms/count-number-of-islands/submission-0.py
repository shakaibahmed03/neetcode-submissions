class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows, cols= len(grid),len(grid[0])
        visit=set()
        islands=0

        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0" or (r,c) in visit:
                return
            
            visit.add((r,c))

            directions=[(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in directions:
                dfs(dr+r, dc+c)

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visit:
                    islands+=1
                    dfs(r,c)
        
        return islands
        