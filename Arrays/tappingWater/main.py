height =[8,7,2,1]


def tappingWater(height):
    left ,right = 0, len(height)-1
    
    
    max_area = 0
    
    while left<right:
    
        area = (right-left) * min(height[left],height[right])
        print("area:",area)
        
        max_area = max(area,max_area)
        
        if height[right]<height[left]:
            right -=1
        else:
            left +=1
            
    return max_area
        
            
    

    
    
    
    
    
    

print("Max water:",tappingWater(height))
