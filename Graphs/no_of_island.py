import json

class Solution :
    def numIslands(self,grid):
        row = len(grid)
        col = len(grid[0])
        used = [[False for j in range(col)] for i in range(row)]
        # print(used)
        
        count =0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not  used[i][j]:
                    self.dfs(grid,used ,row,col,i,j)
                    count += 1
                    
        return count
    
    def dfs(self,grid,used,row,col,x,y):
        if grid[x][y] == 0 or used[x][y] :
            return
        
        used[x][y] = True
        
        if x !=0 :
            self.dfs(grid,used ,row,col,x-1,y)
        if x != row-1 :
            self.dfs(grid,used ,row,col,x+1,y)
        if y != col-1 :
            self.dfs(grid,used ,row,col,x,y-1)
        if y != col-1 :
            self.dfs(grid,used ,row,col,x,y+1)
                
        



if __name__ == '__main__':
    s =Solution()
    res= s.numIslands([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])
    res_1 = s.numIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]])
    number_of_islands = {
        "case_1": res,
        "case_2": res_1
    }
    print(json.dumps(number_of_islands))