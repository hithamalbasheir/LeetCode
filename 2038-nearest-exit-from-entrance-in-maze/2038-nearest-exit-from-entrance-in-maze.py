class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        #I should start with a BFS
        #Go into all 4 directions and start counting marking every place I go through as a wall so I don't go into the loophole 
        #Once I find an exit then it's the nearest and I can immediately return the counter, otherwise I'll explore till the queue is empty and return -1 ,meaning there's no solution found
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(maze), len(maze[0])
        #Mark the starting point as a wall
        maze[entrance[0]][entrance[1]] = '+'
        q = [(entrance[0], entrance[1], 0)]
        while q: 
            cur_row, cur_col, cur_dist = q.pop(0)
            for d in directions:
                next_row, next_col = d[0] + cur_row, d[1] + cur_col
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":
                    #Check if it's an exit
                    if next_row == rows - 1 or next_col == cols - 1 or next_row == 0 or next_col == 0:
                        return cur_dist + 1
                    maze[next_row][next_col] = '+'
                    q.append((next_row, next_col, cur_dist +1)) 
        return -1 
