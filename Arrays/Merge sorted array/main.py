nums1 = [2,0]
m = 1
nums2 = [1]
n = 1


def mergeSortedArray(nums1,nums2,m,n):
    
    
    
    first_pointer,second_pointer,write_pointer= m-1,n-1,m+n-1
    
    while second_pointer>=0:
        
        if first_pointer >=0 and nums1[first_pointer]>nums2[second_pointer]:
            nums1[write_pointer] = nums1[first_pointer]
            first_pointer -=1
        else:
            nums1[write_pointer]=nums2[second_pointer]
            second_pointer -=1
            
        write_pointer -=1
        
    return nums1
    
    
    
    



print(mergeSortedArray(nums1,nums2,m,n))
