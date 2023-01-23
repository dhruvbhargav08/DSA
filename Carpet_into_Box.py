#This is from Geeks for Geeks.Question link at last
# There is a carpet of a size a*b [length * breadth]. You are given a box of size c*d. 
# The task is, one has to fit the carpet in the box in a minimum number of moves. 
# In one move, you can either decrease the length or the breadth of the carpet by half (floor value of its half).
# Note: One can even turn the carpet by 90 degrees any number of times, wont be counted as a move.
#User function Template for python3


class Solution:
    def carpetBox(self, a,b,c,d):
        #code here
        flag1=0
        flag2=0
        temp1,temp2=a,b
        while a>c:
            a=a//2
            flag1+=1
        while b>d:
            b=b//2
            flag1+=1
        a,b=temp2,temp1
        while a>c:
            a=a//2
            flag2+=1
        while b>d:
            b=b//2
            flag2+=1
        return min(flag1,flag2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/230d87552a332a2970b2092451334a007f2b0eec/1?page=2&difficulty[]=1&status[]=solved&sortBy=submissions