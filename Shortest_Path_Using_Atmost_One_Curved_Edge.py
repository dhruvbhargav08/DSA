# This is from Geeks for Geeks.Question link at last
# Given an undirected connected graph of n vertices and list of m edges in a graph and for each pair of vertices that are connected by an edge. 
# There are two edges between them, one curved edge and one straight edge i.e. the tuple (x, y, w1, w2) means that between vertices x and y, there is a straight edge with weight w1 and a curved edge with weight w2.
# You are given two vertices a and b and you have to go from a to b through a series of edges such that in the entire path you can use at most 1 curved edge. 
# Your task is to find the shortest path from a to b satisfying the above condition. 
# If there is no path from a to b, return -1.
#User function Template for python3
from heapq import heappop, heappush
from math import inf
class Solution:
    def dijkstra(self, graph, src):
        n = len(graph)
        dist = [inf]*n
        dist[src] = 0
        heap = [(dist[src], src)]
        while heap:
            d, u = heappop(heap)
            if dist[u] < d:
                continue
            for v, wt in graph[u]:
                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heappush(heap, (dist[v], v))
        return dist
    def shortestPath(self, n, m, a, b, edges):
        graph = [[] for _ in range(n)]
        for u, v, w1, _ in edges:
            graph[u-1].append((v-1, w1))
            graph[v-1].append((u-1, w1))
        
        dista = self.dijkstra(graph, a-1)
        distb = self.dijkstra(graph, b-1)
        res = dista[b-1]
        for u, v, _, w2 in edges:
            res = min(res, dista[u-1] + w2 + distb[v-1])
            res = min(res, distb[u-1] + w2 + dista[v-1])
        return res if res != inf else -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 
sys.setrecursionlimit(10**6) 
from heapq import *

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        a,b=map(int,input().split())
        edges = []
        for i in range(m):
            edge = list(map(int,input().split()))
            edges.append(edge)
        
        ob = Solution()
        print(ob.shortestPath(n,m,a,b,edges))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/e7d81a082cda6bd1e959d943197aa3bc21b88bdb/0