target,nums = 7,[2,3,1,2,4,3]

#expected result = 2

def minSubArrayLen(nums,target):
    left=0
    min_len =float('inf')
    curr_sum =0
    
    n = len(nums)
    for right in range(n):
        
        curr_sum +=nums[right]
        
        while curr_sum >= target:
            min_len = min(min_len,right-left+1)
            curr_sum -= nums[left]
            left+=1
    
    return min_len if min_len != float('inf') else 0
    
    
    
    
    
    
print(minSubArrayLen(nums,target))
