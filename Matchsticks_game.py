# This is from Geeks for Geeks.Question link at last
# Two friends, A and B, are playing the game of matchsticks. 
# In this game, a group of N matchsticks is placed on the table. 
# The players can pick any number of matchsticks from 1 to 4 (both inclusive) during their chance. 
# The player who takes the last match stick wins the game. 
# If A starts first, how many matchsticks should he pick on his 1st turn such that he is guaranteed to win the game or determine if it's impossible for him to win. 
# Return -1 if it's impossible for A to win the game, else return the number of matchsticks should he pick on his 1st turn such that he is guaranteed to win.
# Note : Consider both A and B play the game optimally.
#User function Template for python3

class Solution:
    def matchGame(self, N):
         # code here
        if N%5:
            return N%5
        return -1 
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.matchGame(N))
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/-matchsticks-game4906/1