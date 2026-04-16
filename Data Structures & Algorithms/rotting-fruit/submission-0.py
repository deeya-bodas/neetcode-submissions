from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        queue = deque()
        time, fresh_count = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 2):
                    queue.append((i, j))
                elif(grid[i][j] == 1):
                    fresh_count += 1

        # now proceed with a mutli-source BFS
        while(len(queue) > 0 and fresh_count > 0):
            for i in range(len(queue)):
                print(queue)
                r, c = queue.popleft()

                # make sure this item hasn't already become rotten?
                if(r != 0):
                    if (grid[r-1][c] == 1):
                        fresh_count -= 1
                        grid[r-1][c] = 2
                        queue.append((r-1, c))
                if(r != len(grid)-1):
                    if (grid[r+1][c] == 1):
                        fresh_count -= 1
                        grid[r+1][c] = 2
                        queue.append((r+1, c))
                if(c != 0):
                    if (grid[r][c-1] == 1):
                        fresh_count -= 1
                        grid[r][c-1] = 2
                        queue.append((r, c-1))
                if(c != len(grid[r])-1):
                    if (grid[r][c+1] == 1):
                        fresh_count -= 1
                        grid[r][c+1] = 2
                        queue.append((r, c+1))

            time += 1

        # after BFS is complete, check whether or not there are any fresh fruit left
        if(fresh_count > 0):
            return -1
        else:
            return time

            
            
        
        