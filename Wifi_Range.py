#This is from Geeks for Geeks.Question link at last
# There are N rooms in a straight line in Geekland State University's hostel, you are given a binary string S of length N where S[i] = '1' represents that there is a wifi in ith room or S[i] = '0' represents no wifi. 
# Each wifi has range X i.e. if there is a wifi in ith room then its range will go upto X more rooms on its left as well as right. 
# You have to find whether students in all rooms can use wifi.
#User function Template for python3
class Solution:
    def wifiRange(self, N, S, X): 
        #code here
        temp=0
        while temp<N and S[temp]!='1':
            temp+=1
        if temp==N or temp>X:
            return False
        flag=temp
        for i in range (N):
            if i-flag+1>2*(X+1):
                return False
            if S[i]=='1':
                flag=i
        if N-flag>X+1:
            return False
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/61567fb59e9f202db5cc2ad320ffeb6d95bf72d7/1