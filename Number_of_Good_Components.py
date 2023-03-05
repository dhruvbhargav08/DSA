# This is from Geeks for Geeks.Question link at last
# Given an undirected graph with V vertices(numbered from 1 to V) and E edges. 
# Find the number of good components in the graph.
# A component of the graph is good if and only if the component is a fully connected component.
# Note: A fully connected component is a subgraph of a given graph such that there's an edge between every pair of vertices in a component, the given graph can be a disconnected graph. Consider the adjacency list from index 1.
#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        # code here
        ans=0
        super_visited=set()
        def dfs(visted,adj,node,res):
            nonlocal super_visited
            res.append(node)
            visited.add(node)
            super_visited.add(node)
            for node in adj[node]:
                if node not in visited:
                    dfs(visited,adj,node,res)
            return res
        component=[]
        for i in range (1,V+1):
            if i not in super_visited:
                visited=set()
                res=[]
                res=dfs(visited,adj,i,res)
                component.append(res)
        for i in component:
            comlen=len(i)
            count=0
            temp=0
            for j in i:
                temp+=1
                if len(adj[j])<comlen-1:
                    count+=1
                if count>0:
                    break
            if count==0 and temp==comlen:
                ans+=1
        return ans
            
            
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            a,b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
            
        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/1a4b617b70f0142a5c2b454e6fbe1b9a69ce7861/1