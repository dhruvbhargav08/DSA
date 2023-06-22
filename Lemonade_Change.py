# This is from Geeks for Geeks.Question link at last
# You are an owner of lemonade island, each lemonade costs $5. 
# Customers are standing in a queue to buy from you and order one at a time (in the order specified by given array bills[]). 
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. 
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# NOTE: At first, you do not have any bill to provide changes with. 
# You can provide changes from the bills that you get from the previous customers.
# Given an integer array bills of size N where bills [ i ] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        ten,five=0,0
        for i in range (N):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                five-=1
                ten+=1
            else:
                if five>=1 and ten>=1:
                    ten-=1 
                    five-=1
                else:
                    five-=3
            if five<0 or ten<0:
                return False 
        return True 
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/lemonade-change/1