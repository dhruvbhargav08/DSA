#This is from Geeks for Geeks.Question link at last
# You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.
#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if(len(self.s)==0):
            self.s.append(x)
            self.minEle=x
        else:
            if(x>=self.minEle):
                self.s.append(x)
            else:
                self.s.append(x+x-self.minEle)
                self.minEle=x;
    def pop(self):
        #CODE HERE
        if(len(self.s)==0):
            return -1
        temp=self.s[-1]
        flag=0
        if(temp>=self.minEle):
            flag=temp
            self.s.pop()
        else:
            flag=self.minEle
            self.minEle=2*self.minEle-temp
            self.s.pop()
        return flag
    def getMin(self):
        #CODE HERE
        if(len(self.s)==0):
            return -1
        else:
            return self.minEle;


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends
# Question link
# https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions