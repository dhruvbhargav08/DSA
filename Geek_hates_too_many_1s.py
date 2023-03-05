# This is from Geeks for Geeks.Question link at last
# Given an non-negative integer n. 
# You are only allowed to make set bit unset. 
# You have to find the maximum possible value of query so that after performing the given operations, no three consecutive bits of the integer query are set-bits. 
class Solution:
    def noConseBits(self, n : int) -> int:
        # code here
        def tobinary(num):
            listt=[]
            lenn=0
            while num>0:
                listt.append(num%2)
                lenn+=1
                num//=2
            return listt[::-1],lenn
        def todecimal(listt,N):
            res=0
            temp=0
            for i in range (N-1,-1,-1):
                res=res+(2**temp)*listt[i]
                temp+=1
            return res
        binary,lenn=tobinary(n)
        count=0
        for i in range (lenn):
            if binary[i]==1:
                count+=1
            if binary[i]==0:
                count=0
            if count==3:
                binary[i]=0
                count=0
        decimal=todecimal(binary,lenn)
        return decimal
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/07e45fe40846bc670ad2507d2c649304699768b9/1