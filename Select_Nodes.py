#This is from Geeks for Geeks.Question link at last
# Given N nodes of a tree and a list of edges. 
# Find the minimum number of nodes to be selected to light up all the edges of the tree.
# An edge lights up when at least one node at the end of the edge is selected.
#User function Template for python3

class Solution:
    def dfs(self, graph, u, p):
        temp, flag = 0, 1    
        for v in graph[u]:
            if v != p:
                count_temp, count_flag = self.dfs(graph, v, u)
                temp += count_flag
                flag += min(count_flag, count_temp)
        return temp, flag
    def countVertex(self, N, edges):
        graph = [[] for _ in range(N)]
        for u,v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        return min(self.dfs(graph, 0, -1))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        edges=[]
        for _ in range(N-1):
            arr = list(map(int,input().split()))
            edges.append(arr)

        ob = Solution()
        print(ob.countVertex(N, edges))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/f7bfa137576243795abb0595962d61b632bbad21/0