# This is from Geeks for Geeks.Question link at last
# Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 
# Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
            def bfs(node):
                from collections import deque
                que = deque([(node,-1)])
                while que:
                    node,prev = que.popleft()
                    for i in adj[node]:
                        if i == prev: continue
                        if not visited[i]:
                            visited[i] = 1
                            que.append((i,node))
                        else: return 1
                return 0
            visited = [0]*V
            for i in range(V):
                if not visited[i]:
                    visited[i] = 1
                    if bfs(i): return 1
            return 0
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/0