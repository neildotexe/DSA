class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr):
        # Using priority queue and minHeap
        heapq.heapify(arr) #Converting into a priority queue
        res = 0
        while len(arr)>1:
            first = heapq.heappop(arr) #Remove first element from minHeap which is smallest 
            second = heapq.heappop(arr) #Remove first element from the resultant minHeap which is the next smallest
            
            res += (first + second)
            
            heapq.heappush(arr, (first+second))
        
        return res
