# This is from Geeks for Geeks.Question link at last
# Given a binary matrix your task is to find all unique rows of the given matrix in the order of their appearance in the matrix.
#User function Template for python3
class Solution():
    def uniqueRow(self,row, col, matrix):
        #complete the function
        listt=[]
        def todecimal(row,col):
            decimal=0
            power=col-1
            for i in row:
                decimal+=i*(2**power)
                power-=1
            return decimal
        def tobinary(num,col):
            listt=[]
            while num>0:
                listt.append(num%2)
                num=num//2
            while len(listt)<col:
                listt.append(0)
            listt.reverse()
            return listt
        for i in range (row):
            decimal=todecimal(matrix[i],col)
            if decimal not in listt:
                listt.append(decimal)
        ans=[]
        for i in listt:
            ans.append(tobinary(i,col))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = [[None for _ in range(col)]for _ in range(row)]
        s = input().split()
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(s[i*col+j])
        
        ob = Solution()
        a = ob.uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/unique-rows-in-boolean-matrix/1