# This is from Geeks for Geeks.Question link at last.
# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
#User function Template for python3


class Solution:
    def dfs(self, node, V, adj, visited, pathvisited):
        visited[node] = True
        pathvisited[node] = True
        for i in adj[node]:
            if not visited[i]:
                if self.dfs(i, V, adj, visited, pathvisited):
                    return True
            elif pathvisited[i]:
                return True
        pathvisited[node] = False
        return False
    def isCyclic(self, V, adj):
        visited = [False] * V
        pathvisited = [False] * V
        for i in range(V):
            if not visited[i]:
                if self.dfs(i, V, adj, visited, pathvisited):
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?page=1&difficulty[]=1&status[]=unsolved&sortBy=submissions