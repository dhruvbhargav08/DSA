# This is from Geeks for Geeks.Question link at last
# Given a character array tasks of size N, representing the tasks a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time. 
# For each unit of time, the CPU could complete either one task or just be idle.
# CPU has a cooldown period for each task. 
# CPU can repeat a task only after atleast K units of time has passed after it did same task last time. 
# It can perform other tasks in that time, can stay idle to wait for repeating that task.
# Return the least number of units of times that the CPU will take to finish all the given tasks.
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def leastInterval(self, N, K, tasks):
        # Code here
        listt=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        mapp={}
        for i in listt:
            mapp[i]=0
        for i in range (N):
            mapp[tasks[i]]+=1
        maxx=max(mapp.values())
        ans=(K+1)*(maxx-1)
        for i in mapp.values():
            if maxx==i:
                ans+=1
        return max(ans,N)
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/task-scheduler/1