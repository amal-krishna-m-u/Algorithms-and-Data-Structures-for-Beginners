from collections import defaultdict

def sumOfFlooredPairs(nums)->int:
    
    sum_of_floored_pairs=0
    MOD = 10**9+7
    
    count = defaultdict(int)
    max_num = max(nums)
    #prefix_sum
    range_till_n=[0] * (max_num+1)
    
    for num in nums:
        count[num]+=1
    
    for i in range(1,max_num+1):
        range_till_n[i] = range_till_n[i-1] + count[i]
    
    
    for num in count:
        # for every number btwn 3 to 6 (not including 6) x/3 ==1 , now if you multiply 3*2 ie 6-9 it will be 2 so k is that constant
        k=1
        
        while num*k<=max_num:
            start = num*k
            end=min(num * (k+1)-1,max_num)
            sum_of_floored_pairs += (range_till_n[end]-range_till_n[start-1]) * k * count[num]
            k+=1

    
    return sum_of_floored_pairs
    
    
    

#test case 1 
nums1 = [7,7,7,7,7,7,7]
nums2 = [2,5,9]


print("input:",nums1,"output:")
print(sumOfFlooredPairs(nums1))
print("input:",nums2,"output:")
print(sumOfFlooredPairs(nums2))
