#This is from Geeks for Geeks.Question link at last
# Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. 
# Find the minimum number of coins to make the change. 
# If not possible to make change then return -1.
#User function Template for python3
class Solution:
	def minCoins(self, coins, M, V):
		# code here
            dp = [float('inf')] * (V + 1) 
            dp[0] = 0 

            for i in range(1, V + 1):
                for coin in coins:
                    if coin <= i:
                        dp[i] = min(dp[i], dp[i - coin] + 1)

            if dp[V] == float('inf'):
                return -1  
            else:
                return dp[V]  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/number-of-coins1824/1?page=1&difficulty[]=1&status[]=unsolved&category[]=Dynamic%20Programming&sortBy=submissions