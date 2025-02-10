def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

    window =set()

    left=0


    for right in range(len(nums)):

        if right-left>k:
            window.remove(nums[left])
            left+=1
        if nums[right] in window and right-left<=k:
            return True
        
        window.add(nums[right])
    
    return False
    
    


nums = [1,2,3,1]
k = 3

#expected output : true


print("output:",containsNearbyDuplicate(nums,k))