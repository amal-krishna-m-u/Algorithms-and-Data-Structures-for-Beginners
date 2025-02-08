nums=[-2,1,-3,4,-1,2,1,-5,4]
# expected output = 6


def maxSubArray(nums):
    max_sum = float('-inf')
    curr_sum = 0
    
    for num in nums:
        curr_sum = max(curr_sum,0) + num
        max_sum = max(curr_sum,max_sum)
    return max_sum
        
 
    
print(maxSubArray(nums))