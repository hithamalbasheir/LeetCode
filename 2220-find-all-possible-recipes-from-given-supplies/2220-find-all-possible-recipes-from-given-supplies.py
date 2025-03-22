class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        indegree = [0] * n
        supplies_set = set(supplies)
        heap = []
        q = deque([])
        dependency_graph = defaultdict(list)
        for i in range(n):
            indegree[i] = len(ingredients[i])
            for ing in ingredients[i]:
                if ing in supplies_set:
                    indegree[i] -= 1
                else:
                    dependency_graph[ing].append(i)
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            i = q.popleft()
            res.append(recipes[i])
            for idx in dependency_graph[recipes[i]]:
                indegree[idx] -= 1
                if indegree[idx] == 0:
                    q.append(idx)
        return res