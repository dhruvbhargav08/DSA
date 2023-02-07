#This is from Geeks for Geeks.Question link at last
# Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
# Note: One can move from node u to node v only if there's an edge from u to v and find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the graph. 
# Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.
#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited=[False]*V
        queue=[]
        res=[0]
        queue.append(0)
        visited[0]=True
        while queue:
            w=queue.pop(0)
            for i in adj[w]:
                if visited[i]==False:
                    queue.append(i)
                    res.append(i)
                    visited[i]=True
        return res


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")

      

# } Driver Code Ends


# Question link
# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?page=1&difficulty[]=0&status[]=solved&sortBy=submissions
  
