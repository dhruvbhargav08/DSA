#This is from Geeks for Geeks.Question link at last
# Given a string str consisting of only two characters 'a' and 'b'. 
# You need to find the minimum steps required to make the string empty by removing consecutive a's and b's.
class Solution:
    def minSteps(self, strr : str) -> int:
        # code here
        count1,count2=0,0
        n=len(strr)
        for i in range(1,n):
            if strr[i-1]=='a' and strr[i]=='b' :
                count1+=1
            if strr[i-1]=='b' and strr[i]=='a' :
                count2+=1
        if strr[0]==strr[n-1]:
            return min(count1,count2)+1
        return min(count1,count2)+2



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/6a1b365b520f10c8a29b533eb72951b4b4237b57/1