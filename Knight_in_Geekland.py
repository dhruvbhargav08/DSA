#This is from Geeks for Geeks.Question link at last
# Knight is at (start_x,start_y) in Geekland which is represented by an NxM 2D matrix.
# Each cell in the matrix contains some points. 
# In the ith step, the knight can collect all the points from all the cells that can be visited in exactly i steps without revisiting any cell.
# Also, the knight has some magical powers that enable him to fetch coins from the future i.e. If the knight can collect y coins in the xth step he can fetch all the coins that he will collect in the (x + y)th step and if the knight can collect z coins in the yth step he can fetch all the coins that he will collect in the (y + z)th step and so on without increasing the step count i.e. knight will stay on xth step and will get all the coins of the future steps mentioned above((x + y)th step coins + (y+z)th steps + ...).
# Find the minimum number of steps required to collect the maximum points.
# Note: The knight moves exactly the same as the knight on a chess board. Please follow 0 indexing.
#User function Template for python3

class Solution:
    def knightInGeekland(self, arr, start):
        n,m=len(arr),len(arr[0])
        listt=[]
        lenn=0
        queue=[start]
        while queue:
            temp=0
            q=[]
            for pos in queue:
                if arr[pos[0]][pos[1]]>-1:
                    temp+=arr[pos[0]][pos[1]]
                    arr[pos[0]][pos[1]]=-1
                    if pos[0]-2>-1 and pos[1]-1>-1:
                        q.append([pos[0]-2,pos[1]-1])
                    if pos[0]-2>-1 and pos[1]+1<m:
                        q.append([pos[0]-2,pos[1]+1])
                    if pos[0]-1>-1 and pos[1]+2<m:
                        q.append([pos[0]-1,pos[1]+2])
                    if pos[0]+1<n and pos[1]+2<m:
                        q.append([pos[0]+1,pos[1]+2])
                    if pos[0]+2<n and pos[1]+1<m:
                        q.append([pos[0]+2,pos[1]+1])
                    if pos[0]+2<n and pos[1]-1>-1:
                        q.append([pos[0]+2,pos[1]-1])
                    if pos[0]+1<n and pos[1]-2>-1:
                        q.append([pos[0]+1,pos[1]-2])
                    if pos[0]-1>-1 and pos[1]-2>-1:
                        q.append([pos[0]-1,pos[1]-2])
            queue=q
            listt.append(temp)
            lenn+=1
        ans,res=listt[0],0
        for i in range(lenn-1,-1,-1):
            if i+listt[i]<lenn:
                listt[i]+=listt[i+listt[i]]
            if ans<=listt[i]:
                ans=listt[i]
                res=i
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,m = map(int, input().split())
        starting_x, starting_y = map(int, input().split())
        orignal_array = []

        for i in range(n):
            l = list(map(int, input().split()))
            orignal_array.append(l)

        res = Solution().knightInGeekland(orignal_array, [starting_x, starting_y])
        print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/7e5ec07f9d865297cff9a91522c2ce805433b420/1