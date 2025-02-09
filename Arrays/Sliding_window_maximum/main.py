nums = [1,3,-1,-3,5,3,6,7]
k = 3
# expected Output: [3,3,5,5,6,7]


from collections import deque

def maxSlidingWindow(nums,k):
    
    if not nums:
        return []
    
    results =[]
    
    index_q = deque()
    
    
    for index,num in enumerate(nums):
        
        if index_q and index_q[0]<index-k+1:
            index_q.popleft()
        
        while index_q and nums[index_q[-1]] < num:
            index_q.pop()
        
        index_q.append(index)
        
        
        if index>=k-1:
            results.append(nums[index_q[0]])
    
    return results
    
    
    

print("output:",maxSlidingWindow(nums,k))