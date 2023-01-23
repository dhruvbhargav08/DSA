#This is from Geeks for Geeks.Question link at last
# Stickler the thief wants to loot money from a society having n houses in a single line. 
# He is a weird person and follows a certain rule when looting the houses. 
# According to the rule, he will never loot two consecutive houses. 
# At the same time, he wants to maximize the amount he loots. 
# The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. 
# He asks for your help to find the maximum money he can get if he strictly follows the rule. 
# Each house has a[i]amount of money present in it.
#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        temp=a[0]
        flag=0
        var=0
        for i in range (1,n):
            if temp>flag:
                var=temp
            else:
                var=flag
            temp=flag+a[i]
            flag=var
        if temp>flag:
            return temp
        else:
            return flag

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions