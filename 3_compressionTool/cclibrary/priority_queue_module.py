# A simple implementation of Priority Queue
# using Queue.
# Class inherits from Object
# whereas now python it get inherited implictly
class PriorityQueue(object):
    def __init__(self,arr=[]):
        #default arr is empty if not provided
        self.queue = []
        for i in range(len(arr)):
            self.insert(arr[i])
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

        #now reorder up
        # 0 : 1,2  1 : 3,4
        curr=len(self.queue)-1
        parent=(int)((curr-1)/2)

        #making max heap so child is more than parent
        while (curr>0 and self.queue[parent]<self.queue[curr]):
            self.queue[parent],self.queue[curr]=self.queue[curr],self.queue[parent]
            curr=parent
            parent=(int)((curr-1)/2)

        print(self)
 
    # for popping an element based on Priority
    #swap front with back
    # then pop_back last that was the top
    # heapify it again

    def delete(self):
        item =self.queue[0]

        n=len(self.queue)
        self.queue[0],self.queue[n-1]=self.queue[n-1],self.queue[0]
        self.queue.pop()
        n=len(self.queue) #new size 

        #now stabalize the top
        #for max heap
        curr=0
        
        while( curr<n):
            left=2*curr +1
            right=2*curr+2
            if(left>=n): break
            if(right>=n):
                if(self.queue[left]>self.queue[curr]):
                    self.queue[curr],self.queue[left]=self.queue[left],self.queue[curr]
                    curr=left
                    continue
            
            maxIndex=left
            if(self.queue[left]<self.queue[right]): maxIndex=right
            if(self.queue[maxIndex]>self.queue[curr]):
                self.queue[curr],self.queue[maxIndex]=self.queue[maxIndex],self.queue[curr]
                curr=maxIndex
                continue
        return item



        
    # brute implmentation
    def delete_brute(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()


if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)            
    while not myQueue.isEmpty():
        print(myQueue.delete()) 


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