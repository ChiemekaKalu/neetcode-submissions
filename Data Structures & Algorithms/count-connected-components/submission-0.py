from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def buildGraph(edges):
            graph = defaultdict(list)
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        def bfs(graph, node, visited):
            q = deque()
            q.append(node)
            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            return 
        
        visited = set()
        graph = buildGraph(edges)
        res = 0 
        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(graph, node, visited)
                res += 1
        return res