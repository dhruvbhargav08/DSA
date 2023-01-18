#This is from Geeks for Geeks.Question link at last
# Given a matrix of size r*c. Traverse the matrix in spiral form.
#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        listt=[0]*r*c
        list_index=0
        direction=0
        up,down,left,right=0,r-1,0,c-1
        while left<=right and up<=down:
            if direction==0:
                for i in range (left,right+1):
                    listt[list_index]=matrix[up][i]
                    list_index+=1
                up+=1
            elif direction==1:
                for i in range(up,down+1):
                    listt[list_index]=matrix[i][right]
                    list_index+=1
                right-=1
            elif direction==2:
                for i in range(right,left-1,-1):
                    listt[list_index]=matrix[down][i]
                    list_index+=1
                down-=1
            elif direction==3:
                for i in range(down,up-1,-1):
                    listt[list_index]=matrix[i][left]
                    list_index+=1
                left+=1
            direction=(direction+1)%4
        return listt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions