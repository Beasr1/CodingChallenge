# A simple implementation of Priority Queue
# using Queue.
# Class inherits from Object
# whereas now python it get inherited implictly

'''
my custom comparator
(top,newElement)
if true then swap
else do not

so
lambda x,y : x<y #default x<y
top<ele than swap means max heap
'''
class PriorityQueue(object):
    def __init__(self,arr=None,comparator=None):
        #default arr is empty if not provided
        self.queue = []
        self.compare=comparator
        if not(comparator): self.compare=lambda top,ele : top<ele #default x<y
        if arr:
            for i in range(len(arr)):
                self.insert(arr[i])
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    def __swap(self,i,j):
        self.queue[i],self.queue[j]=self.queue[j],self.queue[i]

 
    # for inserting an element in the queue
    def insert(self, data):
        if not callable(self.compare):
            raise ValueError("Comparator must be a callable function")
        self.queue.append(data)
        self.__heapify_up() #now reorder up
        
    def __heapify_up(self):
        curr=len(self.queue)-1
        parent=(int)((curr-1)/2)

        #making max heap so child is more than parent
        #self.queue[parent]<self.queue[curr]
        while (curr>0 and self.compare(self.queue[parent],self.queue[curr])):
            if(not isinstance(self.compare(self.queue[parent],self.queue[curr]),bool)):
                raise ValueError("Comparator must return a boolean value")
            
            self.__swap(parent,curr)
            curr=parent
            parent=(int)((curr-1)/2)

 
    # for popping an element based on Priority
    #swap front with back
    # then pop_back last that was the top
    # heapify it again

    def delete(self):
        if(self.isEmpty()): return None

        item =self.queue[0]
        self.__swap(0,len(self.queue)-1)
        self.queue.pop()
        self.__heapify_down() #now stabalize the top : for max heap
        return item
    
    def __heapify_down(self):
        n=len(self.queue) #new size 
        curr=0
        
        while( curr<n):
            left=2*curr +1
            right=2*curr+2
            if(left>=n): break
            if(right>=n):
                #self.queue[curr]<self.queue[left]
                comp=self.compare(self.queue[curr],self.queue[left])
                if(not isinstance(comp,bool)):
                    raise ValueError("Comparator must return a boolean value")

                if(comp):
                    self.__swap(left,curr)
                    curr=left
                    continue
            
            maxIndex=left

            #self.queue[left]<self.queue[right] : default
            comp=self.compare(self.queue[left],self.queue[right])
            if(not isinstance(comp,bool)):
                raise ValueError("Comparator must return a boolean value")
            if(comp): maxIndex=right

            #self.queue[curr]<self.queue[maxIndex] : default
            comp=self.compare(self.queue[curr],self.queue[maxIndex])
            if(not isinstance(comp,bool)):
                raise ValueError("Comparator must return a boolean value")
            if(comp):
                self.__swap(maxIndex,curr)
                curr=maxIndex
                continue




# if __name__ == '__main__':
#     myQueue = PriorityQueue()
#     myQueue.insert(12)
#     myQueue.insert(1)
#     myQueue.insert(14)
#     myQueue.insert(7)
#     print(myQueue)            
#     while not myQueue.isEmpty():
#         print(myQueue.delete()) 


'''
inbuilt implmentation
https://www.geeksforgeeks.org/binary-heap/ 
import heapq
li=[1,2,4,5]
heapq.heapify(li)
heapq.heappush(li,4)
heapq.heappop(li)

or

from queue import PriorityQueue

I want to make my own though
''' 