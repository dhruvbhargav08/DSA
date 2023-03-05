# This is from Geeks for Geeks.Question link at last
# Geek is a chemical scientist who is performing an experiment to find an antidote to a poison. 
# The experiment involves mixing some solutions in a flask. 
# Based on the theoretical research Geek has done, he came up with an n * 2 array 'mix', where mix[i] = {X, Y} denotes solutions X and Y that needs to be mixed.
# Also, from his past experience, it has been known that mixing some solutions leads to an explosion and thereby completely ruining the experiment. 
# The explosive solutions are also provided as a m * 2 array 'danger' where danger[i] = {P, Q} denotes that if somehow solutions P and Q get into the same flask it will result in an explosion.
# Help the Geek by returning an array 'answer' of size n, where answer[i] = "Yes" if it is safe to mix solutions in 'mix[i]' or else answer[i] = "No".
# Note: Geek should follow the order of mixing of solutions as it is in 'mix' otherwise the antidote will be ineffective. 
# Also, Geek will not mix the solutions in 'mix[i]' once he gets to know that mixing them will result in an explosion. 
# Mixing a solution will effect the other solutions which will appear after it.
#User function Template for python3

class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        #code here
        parent=[0]*(n+1)
        rank=[0]*(n+1)
        for i in range(n+1):
            parent[i]=i
        def find(x):
            nonlocal parent,rank
            if parent[x]==x:
                return x
            return find(parent[x])
        def union(x,y):
            nonlocal parent,rank
            xref=find(x)
            yref=find(y)
            if xref==yref:
                return 
            if rank[xref]<rank[yref]:
                parent[xref]=yref
            elif rank[xref]>rank[yref]:
                parent[yref]=xref
            else:
                parent[yref]=xref
                rank[xref]+=1
        ans=[]
        for i in range (n):
            a=find(mix[i][0])
            b=find(mix[i][1])
            canmix=True
            for j in range (m):
                c=find(danger[j][0])
                d=find(danger[j][1])
                if (a==c and b==d) or (a==d and b==c):
                    canmix=False
                    break
            if canmix:
                union(a,b)
                ans.append("Yes")
            else:
                ans.append("No")
        return ans
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        mix = [[0 for _ in range(2)] for _ in range(n)]
        danger = [[0 for _ in range(2)] for _ in range(m)]
        for i in range(n+m):
            if i < n:
                a,b = map(int, input().split())
                mix[i][0] = a
                mix[i][1] = b
            else:
                a,b = map(int, input().split())
                danger[i-n][0] = a
                danger[i-n][1] = b
        
        obj=Solution()
        print(*obj.avoidExlosion(mix, n, danger, m))
        
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/d3fd6eb758469ab11e1a812220740d1f9819be70/1 