class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
      memo = {}  # To store paths from each node to the target

      def dfs(node):
          # If this is the target node, return the path containing just this node
          if node == len(graph) - 1:
              return [[node]]
          
          # If we've already computed paths from this node, return them
          if node in memo:
              return memo[node]
          
          paths = []
          # Explore neighbors
          for neighbor in graph[node]:
              for path in dfs(neighbor):
                  paths.append([node] + path)
          
          # Store the paths in memo and return
          memo[node] = paths
          return paths

      return dfs(0)

