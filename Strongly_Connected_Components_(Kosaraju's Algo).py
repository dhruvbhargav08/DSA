# This is from Geeks for Geeks.Question link at last
# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges. 
# Find the number of strongly connected components in the graph.
#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        stack=[]
        visited=[0]*V
        def dfs(node,adj):
            nonlocal visited,stack
            visited[node]=1
            for i in adj[node]:
                if visited[i]==0:
                    dfs(i,adj)
            stack.append(node)
        def transpose(adj):
            newadj=[[]for i in range (V)]
            for i in range (V):
                for j in adj[i]:
                    newadj[j].append(i)
            return newadj
        for i in range (V):
            if visited[i]==0:
                dfs(i,adj)
        adj=transpose(adj)
        def newdfs(stack,node):
            nonlocal visited
            visited[node]=1
            for i in adj[node]:
                if visited[i]==0:
                    dfs(i,adj)
        visited=[0]*V
        count=0
        while stack:
            node=stack.pop()
            if visited[node]==0:
                count+=1
                newdfs(stack,node)
        return count
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
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
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1?page=3&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions