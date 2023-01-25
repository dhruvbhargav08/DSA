# This is from Geeks for Geeks.Question link at last
# Given an array of positive numbers, 
# the task is to find the number of possible contiguous subarrays having product less than a given number k.
#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        low,high=0,0
        count=0
        product=1
        for high in range(n):
            product*=a[high]
            while low<high and product>=k:
                product/=a[low]
                low+=1
            if product<k:
                length=high-low+1
                count+=length
        return count
        
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k1708/0