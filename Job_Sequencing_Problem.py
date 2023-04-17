#This is from Geeks for Geeks.Question link at last
# Given a set of N jobs where each jobi has a deadline and profit associated with it. 
# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. 
# We earn the profit if and only if the job is completed by its deadline. 
# The task is to find the number of jobs done and the maximum profit.
# Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.
#User function Template for python3
from operator import itemgetter
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        # code here
        Jobs.sort(key=lambda x: (-x.profit,x.deadline))
        maxx,count,ans=0,0,0
        for i in Jobs:
            maxx=max(maxx,i.deadline)
        check=[False]*maxx
        for i in Jobs:
            d=i.deadline
            d-=1
            for j in range(d,-1,-1):
                if check[j]!=True:
                    check[j]=True
                    ans+=i.profit
                    count+=1
                    break
        return [count,ans]
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/00ae30d0e0f6d8877c68f8b8558c5b0138fdb4b7/1