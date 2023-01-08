#This is from Geeks for Geeks.Question link at last
# Given an array arr[] of N non-negative integers representing the height of blocks. 
# If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

class Solution:
    def trappingWater(self, arr,n):
        #Code here
        stack = []
        res = 0
        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                pop = stack.pop()
                if stack:
                    left = arr[stack[-1]]
                    right = arr[i]
                    res += (min(right, left) - arr[pop])*(i-stack[-1]-1)
                    
            stack.append(i)
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions