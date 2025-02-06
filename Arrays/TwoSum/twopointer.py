#input
nums=[2,5,8,3,7,15,25]
target = 9
#expected output 
# [0,4] or [4,0]



def twoSum(nums,target)->list:
    left,right=0,len(nums)-1

    sorted_nums = [[i,n] for i,n in enumerate(nums)]
    sorted_nums = sorted(sorted_nums,key = lambda x:x[1])
    print(sorted_nums)

    while left<right:
        curr_sum = sorted_nums[left][1] + sorted_nums[right][1]
    
        if curr_sum > target:
            right -=1
        elif curr_sum < target:
            left +=1
        else:
            return [sorted_nums[left][0],sorted_nums[right][0]]
        
    return []
    
print(twoSum(nums,target))

