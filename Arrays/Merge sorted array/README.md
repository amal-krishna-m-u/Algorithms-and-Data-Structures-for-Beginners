# Merge Sorted Array – Detailed Explanation

This code snippet tackles the classic problem of merging two sorted arrays into one sorted array in-place. The arrays are given as:

- **`nums1`**: The first array, which has extra space at the end to accommodate the elements from `nums2`.  
- **`nums2`**: The second array, which contains sorted elements to be merged into `nums1`.

In our example:
- `nums1 = [2, 0]` with `m = 1` (first element is valid)
- `nums2 = [1]` with `n = 1` (all elements are valid)

The goal is to merge `nums2` into `nums1` so that `nums1` becomes a single sorted array.

---

## Code Listing

```python
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1

def mergeSortedArray(nums1, nums2, m, n):
    # Initialize three pointers:
    # first_pointer: Last valid element index in nums1
    # second_pointer: Last element index in nums2
    # write_pointer: Last index of nums1 (which has size m + n)
    first_pointer, second_pointer, write_pointer = m - 1, n - 1, m + n - 1
    
    # Iterate until all elements from nums2 have been merged
    while second_pointer >= 0:
        # Compare elements from the end of nums1 and nums2
        if first_pointer >= 0 and nums1[first_pointer] > nums2[second_pointer]:
            nums1[write_pointer] = nums1[first_pointer]
            first_pointer -= 1
        else:
            nums1[write_pointer] = nums2[second_pointer]
            second_pointer -= 1
        write_pointer -= 1
        
    return nums1

print(mergeSortedArray(nums1, nums2, m, n))
```

---

## Detailed Explanation

### Overview of the Approach

The strategy is to merge from the end of the arrays to avoid overwriting any elements in `nums1` that haven't been processed yet. Three pointers are used to track positions:

- **`first_pointer`**: Points to the last valid element in `nums1` (initialized to `m - 1`).
- **`second_pointer`**: Points to the last element in `nums2` (initialized to `n - 1`).
- **`write_pointer`**: Points to the last index of `nums1`, where the next largest element should be placed (initialized to `m + n - 1`).

### Step-by-Step Process

1. **Initialization of Pointers:**
   - `first_pointer = m - 1`: Points to the last valid number in `nums1`.
   - `second_pointer = n - 1`: Points to the last number in `nums2`.
   - `write_pointer = m + n - 1`: Points to the last available position in `nums1` (which has been pre-allocated with extra space).

2. **Merging Process (While Loop):**
   - **Loop Condition:**  
     The loop continues as long as `second_pointer` is not negative. This ensures every element in `nums2` is processed.
   
   - **Comparison and Writing:**
     - **Case 1:**  
       If `first_pointer` is valid (i.e., `>= 0`) and `nums1[first_pointer]` is greater than `nums2[second_pointer]`, the larger element (`nums1[first_pointer]`) is placed at the `write_pointer` position. Then, `first_pointer` is decremented to consider the next element.
       
     - **Case 2:**  
       Otherwise, the element from `nums2` (`nums2[second_pointer]`) is placed at the `write_pointer` position, and `second_pointer` is decremented.
     
     - After placing an element, `write_pointer` is decremented to move to the next available slot.
     
3. **Final Result:**
   - Once the loop finishes (i.e., `second_pointer` becomes negative), all elements from `nums2` have been merged into `nums1`. The function returns the merged sorted `nums1`.

### Why Use This Approach?

- **Avoiding Overwrites:**  
  By starting from the end, you ensure that existing elements in `nums1` are not overwritten before being compared.
  
- **Efficiency:**  
  This in-place merging requires only constant extra space and a single pass through the arrays, leading to an overall time complexity of O(m+n).

---

## Other Important Info

### Key Concepts and Inbuilt Functions

- **Three-Pointer Technique:**
  - **Purpose:**  
    Utilizes three pointers to efficiently merge two arrays by working from the end of the arrays to avoid unnecessary data movement.
  - **Use Case:**  
    Commonly used in merging sorted arrays or lists where one array has additional space for merging.

- **Comparison Operators:**
  - **Purpose:**  
    Fundamental operators (`>`, `<`) are used to compare the elements of the arrays to decide which element is larger.
  - **Use Case:**  
    They determine the order in which elements are placed into the merged array.

- **Arithmetic Operations:**
  - **Purpose:**  
    Used to calculate positions and to perform pointer adjustments.
  - **Use Case:**  
    Expressions like `m - 1`, `n - 1`, and `m + n - 1` help in correctly initializing pointers.

This detailed explanation should help you understand not only the code but also the reasoning behind using the three-pointer technique for merging sorted arrays in-place. If you have further questions or need additional clarifications, feel free to ask!