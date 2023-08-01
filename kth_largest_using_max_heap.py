class Heap:
    def __init__(self,A,N):
        self.A=A
        self.heap_size=N
    def max_heapify(self,i):
        l=2*i
        r=2*i+1
        smallest=i
        if ((l < self.heap_size) and
                (self.A[l] > self.A[smallest])):
            smallest = l
        if ((r < self.heap_size) and
                (self.A[r] > self.A[smallest])):
            smallest = r
        if smallest != i:
            self.A[i], self.A[smallest] = (
                self.A[smallest], self.A[i])
            self.max_heapify(smallest) 
    def build_heap(self):
        for i in range (len(self.A)//2+1,-1,-1):
            self.max_heapify(i)
    def findk(self,k):
        self.build_heap()
        for i in range (k-1):
            self.A.pop(0)
            self.max_heapify(0)
        print(self.A[0])
listt=[2,4,1,5,7,5,6,3,2,4,56,3,43,67,69]
obj=Heap(listt,len(listt))
obj.build_heap()
print(obj.A)
obj.findk(3)
print(obj.A)
