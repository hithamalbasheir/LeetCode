class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Topological sort / Kahn's Algorithm
        in_degree = [0] * numCourses
        dependents = defaultdict(list)
        q = []
        res = []

        for i,j in prerequisites:
            in_degree[i] += 1
            dependents[j].append(i)

        for i,j in enumerate(in_degree):
            if j == 0:
                q.append(i)

        while q:
            course = q.pop(0)
            res.append(course)
            for dependent in dependents[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    q.append(dependent)

        return res if len(res) == numCourses else []





