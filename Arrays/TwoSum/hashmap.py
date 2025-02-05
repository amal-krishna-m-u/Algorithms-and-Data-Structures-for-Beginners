#input
nums=[2,7,15,25]
target = 9
#expected output 
# [0,1] or [1,0]
def twoSum(nums,target):
    remaining={}
    
    for index,num in enumerate(nums):
        balance = target - num
        
        if balance in remaining:
            return [index,remaining[balance]]
        else:
            remaining[num]=index
    return []


print("Two sum result:",twoSum(nums,target))
    
