# This is from Geeks for Geeks.Question link at last
# Given a collection of Intervals, the task is to merge all of the overlapping Intervals.
class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
            begin=[]
            finish=[]
            ans=[]
            for i in Intervals:
                begin.append(i[0])
                finish.append(i[1])
            begin.sort()
            finish.sort()
            n=len(begin)
    # 		print(start,finish)
            i,j,start,end=1,0,0,0
            while i<n:
                if begin[i]<=finish[j]:
                    i+=1
                    j+=1
                    end=j
                elif begin[i]>finish[j]:
                    end=j
                    ans.append([begin[start],finish[end]])
                    j+=1
                    end=j
                    start=i
                    i+=1
            ans.append([begin[start],finish[end]])
            return ans
		


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
            n = int(input())
            a = list(map(int, input().strip().split()))
            Intervals = []
            j = 0
            for i in range(n):
                x = a[j]
                j += 1
                y = a[j]
                j += 1
                Intervals.append([x,y])
            obj = Solution()
            ans = obj.overlappedInterval(Intervals)
            for i in ans:
                for j in i:
                    print(j, end = " ")
            print()
# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/8a644e94faaa94968d8665ba9e0a80d1ae3e0a2d/1?page=1&difficulty[]=1&status[]=unsolved&curated[]=1&sortBy=submissions