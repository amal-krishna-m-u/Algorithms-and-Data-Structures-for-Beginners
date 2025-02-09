nums1 = [1,-2,3,-2]
#expected output : 3
nums2 = [5,-3,5]

# expected output 10




def maxSubarraySumCircular(nums):
    
    curr_sum =curr_min=total_sum =0
    max_sum =float('-inf')
    min_sum = float('inf')
    
    for num in nums:
        
        curr_sum = max(curr_sum+num,num)
        max_sum = max(curr_sum,max_sum)
        
        curr_min = min(curr_min+num,num)
        min_sum = min(curr_min,min_sum)
        
        
        total_sum +=num
    
    return max(max_sum,total_sum-min_sum if total_sum !=min_sum else total_sum)
    

    


print("output:",maxSubarraySumCircular(nums1))
print("output:",maxSubarraySumCircular(nums2))
