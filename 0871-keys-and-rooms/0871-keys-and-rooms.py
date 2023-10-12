class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #normal DFS
        visited = {0}
        
        def dfs(i):
            for j in rooms[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
                    if len(visited) == len(rooms): return True
            return
        dfs(0)
        return len(visited) == len(rooms)     
        