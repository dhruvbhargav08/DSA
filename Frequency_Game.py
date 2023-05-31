# This is from Geeks for Geeks.Question link at last
# Given an array A of size N. 
# The elements of the array consist of positive integers. 
# You have to find the largest element with minimum frequency.
#User function Template for python3


def LargButMinFreq(arr,n):
    #code here
    maxx=-float('inf')
    minn=float('inf')
    dictt={}
    for i in range (n):
        if arr[i] not in dictt:
            dictt[arr[i]]=1
        else:
            dictt[arr[i]]+=1
    for i in dictt:
        minn=min(dictt[i],minn)
    for i in dictt:
        if dictt[i]==minn:
            maxx=max(maxx,i)
    return maxx
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends
# Qestion link 
# https://practice.geeksforgeeks.org/problems/frequency-game/1