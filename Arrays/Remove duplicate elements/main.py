nums = [0,0,1,1,1,2,2,3,3,4]
# return k 




def removeDuplicate(nums):
    pointer , writer = 0,1
    
    size = len(nums)
    
    while pointer < size -1:
        if nums[pointer] != nums[pointer+1]:
            nums[writer]=nums[pointer+1]
            writer +=1
        pointer +=1
    
    return writer
    
    
    


n = removeDuplicate(nums)
print("output : ",end="")
for i in range(n):
    print(nums[i],",",end="")
print("\nExpected : 0,1,2,3,4")








