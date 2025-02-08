nums=[-1,0,1,2,-1,-4]
target =0




def threeSum(nums):
    sorted_nums = sorted(nums)
    size = len(sorted_nums)
    
    result =[]
    
    for fixed in range(size-2):
        
        if fixed >0 and sorted_nums[fixed] == sorted_nums[fixed-1]:
            continue
        
        
        low , high = fixed+1,size-1
        
        while low<high:
            
            curr_sum = sorted_nums[fixed] + sorted_nums[low] +sorted_nums[high]
            
            if curr_sum > 0:
                high -=1
            elif curr_sum<0:
                low+=1
                
            else:
                result.append([sorted_nums[fixed] ,sorted_nums[low] ,sorted_nums[high]])
                
                while low<high and sorted_nums[low] == sorted_nums[low+1]:
                    low +=1
                while low<high and sorted_nums[high] == sorted_nums[high -1]:
                    high -=1
                low +=1
                high -=1
    
    return result
                
                
print(threeSum(nums))
