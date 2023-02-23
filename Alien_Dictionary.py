#This is from Geeks for Geeks.Question link at last
# Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. 
# Find the order of characters in the alien language.
# Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
#User function Template for python3

class Solution:
    def findOrder(self,dictt, N, K):
    # code here
        listt=[]
        graph = [[] for i in range(27)]
        q,ind,freq,ans = [],[0]*27,[0]*27,""
        for i in range(N-1):
            str1,str2 = dictt[i],dictt[i+1]
            j,n,m=0,len(str1),len(str2)
            while j < min(n,m):
                if str1[j] != str2[j]:break
                else : j+=1
            if j== n or j==m:continue
            graph[ord(str1[j])-ord('a')].append(ord(str2[j])-ord('a'))
        def topological_sort(graph,k)->list:
            ordering=[]
            visited=set()
            def visit(graph,vertex):
                nonlocal visited,k,ordering
                if vertex in visited:
                    return 
                visited.add(vertex)
                for i in graph[vertex]:
                        visit(graph,i)
                ordering.insert(0,vertex)
            for vertex in range (k):
                visit(graph,vertex)
            return ordering
        listt=topological_sort(graph,K)
        for i in range (K):
            listt[i]=chr(listt[i]+97)
        return listt
        
        
        
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
# Question link 
# https://practice.geeksforgeeks.org/problems/alien-dictionary/0