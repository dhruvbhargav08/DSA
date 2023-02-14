# This is from Geeks for Geeks.Question link at last
# Given a maze with N cells. 
# Each cell may have multiple entry points but not more than one exit(i.e entry/exit points are unidirectional doors like valves).
# You are given an array Edge[] of N integers, where Edge[i] contains the cell number that can be reached from of cell i in one step. 
# Edge[i] is -1 if the ith cell doesn't have an exit. 
# The task is to find the largest sum of a cycle in the maze(Sum of a cycle is the sum of the cell indexes of all cells present in that cycle).
# Note:The cells are named with an integer value from 0 to N-1. If there is no cycle in the graph then return -1.
#User function Template for python3
import sys
sys.setrecursionlimit(10**6)

class Solution():
    def dfs(self, graph, visited, u):
        if visited[u] == 2:
            return -1
        elif visited[u] == 1:
            res, cur = u, u
            while graph[cur] != u:
                cur = graph[cur]
                res += cur
            return res
        elif graph[u] != -1:
            visited[u] = 1
            res = self.dfs(graph, visited, graph[u])
            visited[u] = 2
            return res
        else:
            visited[u] = 2
            return -1
    def largestSumCycle(self, N, Edge):
        #your code goes here
        visited = [0]*N
        res = -1
        for u in range(N):
            res = max(res, self.dfs(Edge, visited, u))
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge=[int(i) for i in input().split()]
        print(Solution().largestSumCycle(N, Edge))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/51afa710a708c0681748445b509696dd588d5c40/0