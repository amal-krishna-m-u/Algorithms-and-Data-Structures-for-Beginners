
# Remove Duplicates from Sorted Array – Detailed Explanation

This code snippet demonstrates how to remove duplicates from a sorted array **in-place**. The function `removeDuplicate` processes the array, ensuring that the first `k` elements (where `k` is returned by the function) contain only unique values. The goal is to update the array without using additional space for another array.

---

## Code Listing

```python
nums = [0,0,1,1,1,2,2,3,3,4]
# The function will return k, the count of unique elements

def removeDuplicate(nums):
    pointer, writer = 0, 1  # pointer for iterating, writer for placing unique elements
    size = len(nums)
    
    while pointer < size - 1:
        # If current element is not equal to the next, it's a unique value
        if nums[pointer] != nums[pointer + 1]:
            nums[writer] = nums[pointer + 1]  # write the unique element at the writer index
            writer += 1  # move the writer to the next position
        pointer += 1  # always move the pointer to the next element
    
    return writer  # writer now represents the count of unique elements

n = removeDuplicate(nums)
print("output : ", end="")
for i in range(n):
    print(nums[i], ",", end="")
print("\nExpected : 0,1,2,3,4")
```

---

## Detailed Explanation

### Overview

- **Input:**  
  A sorted list `nums` that may contain duplicate values.
- **Output:**  
  The function returns an integer `k`, representing the number of unique elements. After running the function, the first `k` elements in `nums` are the unique values in sorted order.

### Step-by-Step Process

1. **Pointer Initialization:**
   - Two pointers are initialized:
     - **`pointer`** is set to `0` and is used to iterate over the array.
     - **`writer`** is set to `1` and indicates the next position in `nums` where a unique element should be placed.
   - **`size`** holds the length of the array, calculated using `len(nums)`.

2. **Iteration and Comparison:**
   - A `while` loop runs as long as `pointer < size - 1`. This condition ensures that the current element and its immediate neighbor can be compared.
   - Inside the loop:
     - **Comparison:**  
       The code checks if `nums[pointer]` is not equal to `nums[pointer + 1]`. Because the array is sorted, duplicates will always be adjacent.
     - **Action on Finding a Unique Element:**  
       If the current element is different from the next one, the unique element `nums[pointer + 1]` is copied to the position indicated by `writer`. The `writer` pointer is then incremented.
     - The `pointer` is always incremented to move through the array.

3. **Return Value:**
   - When the loop finishes, `writer` holds the count of unique elements found. This value is returned and stored in `n`.
   - The main part of the program then prints out the first `n` elements from `nums`, which are the unique values.

### Why This Approach Works

- **Sorted Array Assumption:**
  - Since the input array is already sorted, duplicates appear consecutively. This makes it straightforward to compare adjacent elements and identify unique values.
  
- **In-Place Modification:**
  - Using the `writer` pointer allows the algorithm to overwrite duplicates without requiring extra space for another array.
  
- **Efficiency:**
  - The algorithm makes a single pass through the array, resulting in a time complexity of O(n), which is efficient for this type of problem.

---

## Other Important Info

### Inbuilt Functions and Concepts

- **`len()` Function:**
  - **Purpose:**  
    Computes the number of elements in a list.
  - **Use Case:**  
    Determines the size of the input array, which is used to control the loop iterations.

- **Pointers (Indexing):**
  - **Purpose:**  
    Pointers (or index variables) are used to keep track of positions in the array.
  - **Use Case:**  
    - `pointer`: Iterates over the array to check elements.
    - `writer`: Indicates where to write the next unique element.
  - **Benefit:**  
    This technique allows for in-place updates, which minimizes additional memory usage.

- **While Loop:**
  - **Purpose:**  
    Repeatedly executes the block of code as long as a condition is true.
  - **Use Case:**  
    Continues the process of comparing each element with its neighbor until the end of the array is reached.

This explanation provides a comprehensive look at how the algorithm removes duplicates from a sorted array and why each step is necessary. It also covers the key concepts and inbuilt functions used in the code. If you have any further questions or need additional clarification, feel free to ask!