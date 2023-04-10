#This is from Geeks for Geeks.Question link at last
# N horizontal line segments are arranged on the X-axis of a 2D plane. 
# The start and end point of each line segment is given in a Nx2 matrix lines[ ][ ]. 
# Your task is to find the maximum number of intersections possible of any vertical line with the given N line segments.
#User function Template for python3

class Solution: 
    def maxIntersections(self, lines, N):
        # Code here
        start=[]
        end=[]
        count=0
        res=0
        for i,j in lines:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        i,j=0,0
        while i<N and j<N:
            if start[i]<=end[j]:
                count+=1
                i+=1
            elif start[i]>end[j]:
                count-=1
                j+=1
            res=max(res,count)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        lines=[[] for j in range(N)]
        for j in range(2):
            prr = [int(i) for i in input().split()] 
            for i in range(N): 
                lines[i].append(prr[i])
            
    
        ob = Solution()
        print(ob.maxIntersections(lines, N))
        
        T -= 1

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/63c232252d445a377e01cd91adfd7d1060580038/1