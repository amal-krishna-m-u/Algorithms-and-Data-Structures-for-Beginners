def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    
    left =0
    curr_sum = sum(arr[:k])
    target_sum = k*threshold
    

    count = 1 if curr_sum >=target_sum else 0
    size = len(arr)
    for right in range(k,size,1):
        curr_sum += arr[right]-arr[left]

        if curr_sum>=target_sum:
            count+=1
        
        left+=1
    
    return count
    
    
    
    
    
#input : 
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

# output: 3
