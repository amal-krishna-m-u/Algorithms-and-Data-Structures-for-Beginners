# Three Sum – Detailed Explanation

This code snippet addresses the classic **3 Sum** problem. The goal is to find all unique triplets in an array such that the sum of the triplet is equal to zero. The solution leverages sorting and the two-pointer technique to efficiently find the valid triplets while avoiding duplicates.

---

## Code Listing

```python
nums = [-1, 0, 1, 2, -1, -4]

def threeSum(nums):
    # Sort the list to simplify duplicate handling and two-pointer traversal
    sorted_nums = sorted(nums)
    size = len(sorted_nums)
    
    result = []
    
    # Iterate through the array, fixing one element at a time
    for fixed in range(size - 2):
        # Skip duplicate fixed elements to avoid repeated triplets
        if fixed > 0 and sorted_nums[fixed] == sorted_nums[fixed - 1]:
            continue
        
        # Set two pointers: one starting just after the fixed element, and the other at the end of the array
        low, high = fixed + 1, size - 1
        
        while low < high:
            # Calculate the sum of the triplet
            curr_sum = sorted_nums[fixed] + sorted_nums[low] + sorted_nums[high]
            
            if curr_sum > 0:
                # Sum too high: move the high pointer left to reduce the sum
                high -= 1
            elif curr_sum < 0:
                # Sum too low: move the low pointer right to increase the sum
                low += 1
            else:
                # Found a valid triplet that sums to zero
                result.append([sorted_nums[fixed], sorted_nums[low], sorted_nums[high]])
                
                # Skip over duplicate elements for the low pointer
                while low < high and sorted_nums[low] == sorted_nums[low + 1]:
                    low += 1
                
                # Skip over duplicate elements for the high pointer
                while low < high and sorted_nums[high] == sorted_nums[high - 1]:
                    high -= 1
                
                # Move both pointers after processing a valid triplet
                low += 1
                high -= 1
    
    return result
                
print(threeSum(nums))
```

---

## Detailed Explanation

### 1. Sorting the Array

- **Why:**  
  Sorting the array (using `sorted(nums)`) is crucial because it makes it easier to avoid duplicates and to use the two-pointer technique for finding pairs.
- **Result:**  
  After sorting, the array becomes `[-4, -1, -1, 0, 1, 2]`.

### 2. Fixing One Element and Using Two Pointers

- **Fixing an Element:**  
  The algorithm iterates through the sorted array using a `for` loop. Each iteration fixes one element (`sorted_nums[fixed]`) as the first number of the potential triplet.
- **Avoiding Duplicates for the Fixed Element:**  
  Before processing, the code checks if the current fixed element is the same as the previous one. If so, it skips to avoid generating duplicate triplets.

### 3. Two-Pointer Technique on the Remaining Subarray

- **Setting Up Pointers:**  
  Two pointers (`low` and `high`) are initialized immediately after the fixed element and at the end of the array, respectively.
- **Calculating the Current Sum:**  
  For each fixed element, the sum of the triplet is calculated as:  
  ```python
  curr_sum = sorted_nums[fixed] + sorted_nums[low] + sorted_nums[high]
  ```
  
- **Adjusting Pointers Based on the Sum:**
  - **If `curr_sum` > 0:**  
    The sum is too high, so the `high` pointer is moved left (to a smaller number) to try reducing the sum.
  - **If `curr_sum` < 0:**  
    The sum is too low, so the `low` pointer is moved right (to a larger number) to try increasing the sum.
  - **If `curr_sum` == 0:**  
    A valid triplet is found. It is added to the `result` list.
    
- **Skipping Duplicates for `low` and `high`:**  
  After finding a valid triplet, the code uses inner `while` loops to skip over any duplicate values next to the current `low` and `high` pointers. This ensures that the same triplet is not added multiple times.
  
- **Updating Pointers:**  
  Once duplicates are skipped, both `low` and `high` pointers are adjusted (`low` is incremented and `high` is decremented) to continue searching for other valid pairs with the current fixed element.

### 4. Returning the Result

- After processing all potential triplets, the function returns the `result` list containing all unique triplets that sum to zero.

---

## Other Important Info

### Key Inbuilt Functions and Concepts

- **`sorted()` Function**
  - **Purpose:**  
    Returns a new sorted list from the given iterable.
  - **Use Case:**  
    Sorting is essential for the two-pointer technique and for easily handling duplicates.

- **Two-Pointer Technique**
  - **Purpose:**  
    Efficiently find pairs in a sorted array by starting with two pointers at opposite ends and moving them inward.
  - **Benefits:**  
    This method minimizes the need for nested loops, thereby reducing the time complexity to O(n²) in the worst case.

- **Skipping Duplicates**
  - **Purpose:**  
    To ensure that the output contains only unique triplets.
  - **How:**  
    The code checks for consecutive duplicate values for the fixed element, `low`, and `high` pointers and skips them.

- **While Loop**
  - **Purpose:**  
    Repeatedly executes a block of code until a specified condition is no longer met.
  - **Use Case:**  
    Used here to adjust pointers until a valid triplet is found or until the pointers cross.

This detailed explanation should help you understand how the `threeSum` algorithm works step-by-step, why each decision is made (especially the pointer adjustments and duplicate skipping), and how inbuilt functions and techniques contribute to an efficient solution. If you have further questions or need additional clarification, feel free to ask!