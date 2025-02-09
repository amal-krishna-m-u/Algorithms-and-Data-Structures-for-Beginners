nums=[10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k=19

#expected output :18




def numSubarrayProductLessThanK(nums,k):
    left=0
    curr_product=1
    subarray_len =0
    size = len(nums)
    
    
    if k<=1:
        return 0
    
    for right in range(size):
        curr_product*=nums[right]
        
        while curr_product>=k and right>=left:
            curr_product //=nums[left]
            left+=1
        
        subarray_len+=right-left+1
        
    return subarray_len
            
            
    
    
    
    
    
    
    
    
print("output:",numSubarrayProductLessThanK(nums,k))