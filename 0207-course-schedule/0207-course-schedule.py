class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #DFS approach - basically detecting a cycle here
        #Store all prerequisites in a map
        preMap = defaultdict(list)
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        
        visitMap = set()

        def dfs(crs):
            if crs in visitMap:
                return False
            
            if preMap[crs] == []:
                return True 
            
            visitMap.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visitMap.remove(crs)
            preMap[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True