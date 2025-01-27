class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False] * len(queries)
        
        dependents = [set() for _ in range(numCourses)]
        def dfs(dependency, seen):
            if dependency in seen:
                return set()
            for dependent in dependents[dependency]:
                seen.update(dfs(dependent, seen))
            return dependents[dependency]
                
        for dependency, dependent in prerequisites:
            dependents[dependency].add(dependent)
        for dependency in range(numCourses):
            seen = set()
            for dependent in dependents[dependency]:
                seen.update(dfs(dependent, seen))
            dependents[dependency].update(seen)
        res = []
        for dependency, dependent in queries:
            res.append(dependent in dependents[dependency])
        return res