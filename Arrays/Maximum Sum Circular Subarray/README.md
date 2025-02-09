# Maximum Circular Subarray Sum – Detailed Explanation

In a circular array, the subarray with the maximum sum might either be a standard (non-wrapping) subarray or a circular subarray that wraps from the end of the array to the beginning. This solution uses Kadane's algorithm twice:
- **First**, to find the maximum subarray sum in the usual (non-circular) sense.
- **Second**, to find the minimum subarray sum.  
Then, it computes the maximum circular subarray sum as the total sum of the array minus the minimum subarray sum (provided the entire array isn’t the minimum subarray). Finally, the answer is the maximum of these two values.

---

## Code Listing

```python
nums1 = [1, -2, 3, -2]  # Expected output: 3
nums2 = [5, -3, 5]      # Expected output: 10

def maxSubarraySumCircular(nums):
    # Initialize variables for Kadane's algorithm for maximum sum
    curr_sum = 0
    max_sum = float('-inf')
    
    # Initialize variables for finding the minimum subarray sum
    curr_min = 0
    min_sum = float('inf')
    
    total_sum = 0  # To store the total sum of the array
    
    # Iterate through each number in the array
    for num in nums:
        # Update maximum subarray sum (standard Kadane's algorithm)
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)
        
        # Update minimum subarray sum
        curr_min = min(curr_min + num, num)
        min_sum = min(curr_min, min_sum)
        
        # Add the current number to the total sum
        total_sum += num
    
    # If all numbers are negative, total_sum equals min_sum.
    # Otherwise, total_sum - min_sum gives the sum of the circular subarray.
    # The answer is the maximum of the non-circular and circular subarray sums.
    return max(max_sum, total_sum - min_sum if total_sum != min_sum else total_sum)

print("output:", maxSubarraySumCircular(nums1))
print("output:", maxSubarraySumCircular(nums2))
```

---

## Detailed Explanation

### 1. Problem Overview

- **Objective:**  
  Given a circular array of integers, find the maximum possible sum of a contiguous subarray. The array is considered circular, meaning that the subarray may wrap around the end of the array back to the beginning.

- **Examples:**
  - For `nums1 = [1, -2, 3, -2]`, the maximum subarray sum is `3`.
  - For `nums2 = [5, -3, 5]`, the maximum subarray sum is `10`.

### 2. The Two-Part Approach

#### Part A: Standard Maximum Subarray (Kadane's Algorithm)

- **Goal:**  
  Identify the maximum sum of a contiguous subarray in the non-circular case.
  
- **How It Works:**
  - **`curr_sum`:**  
    Tracks the current subarray sum. For each number, we decide whether to add it to the existing subarray or start a new subarray.
  - **`max_sum`:**  
    Keeps the maximum subarray sum found so far.
  - **Update Rule:**  
    ```python
    curr_sum = max(curr_sum + num, num)
    max_sum = max(curr_sum, max_sum)
    ```

#### Part B: Minimum Subarray Sum

- **Goal:**  
  Identify the minimum contiguous subarray sum. This helps in computing the maximum sum for a circular subarray.
  
- **How It Works:**
  - **`curr_min`:**  
    Tracks the current minimum subarray sum.
  - **`min_sum`:**  
    Stores the smallest subarray sum found.
  - **Update Rule:**  
    ```python
    curr_min = min(curr_min + num, num)
    min_sum = min(curr_min, min_sum)
    ```

#### Total Sum Calculation

- **`total_sum`:**  
  This variable aggregates the sum of all elements in the array. It is used to compute the sum of the subarray that wraps around, which is given by:
  ```python
  total_sum - min_sum
  ```

### 3. Combining the Two Parts

- **Non-Circular Case:**  
  The maximum subarray sum found by Kadane's algorithm is stored in `max_sum`.

- **Circular Case:**  
  The maximum circular subarray sum is calculated as `total_sum - min_sum`. This works because removing the minimum subarray (which might be causing a "dip" in the sum) from the total sum leaves the sum of the wrapping subarray.

- **Edge Case Handling:**  
  If all numbers are negative, then `total_sum` will equal `min_sum`, and the circular approach isn’t valid. In such cases, the answer is simply `max_sum` (which is the least negative number).

- **Final Answer:**  
  The function returns the maximum of the two approaches:
  ```python
  return max(max_sum, total_sum - min_sum if total_sum != min_sum else total_sum)
  ```

---

## Other Important Info

### Key Inbuilt Functions and Concepts

- **`max()` and `min()` Functions:**
  - **Purpose:**  
    Used to update the running maximum (`curr_sum` and `max_sum`) and the running minimum (`curr_min` and `min_sum`).
  - **Benefit:**  
    They allow concise and clear decisions on whether to include the current number in the existing subarray or start fresh.

- **Kadane's Algorithm:**
  - **Concept:**  
    An efficient algorithm for finding the maximum subarray sum in a linear array.
  - **Adaptation for Circular Arrays:**  
    By also finding the minimum subarray sum, we can compute the sum of the "wrapped" subarray.

- **Edge Case Consideration:**
  - **Handling All-Negative Arrays:**  
    If the total sum of the array equals the minimum subarray sum, it indicates that all elements are negative. In such cases, the maximum subarray sum is simply the maximum element.

This explanation should help you understand how the algorithm calculates the maximum circular subarray sum by combining both the standard and circular cases, and why each component of the code is essential. If you have any further questions or need additional clarification, feel free to ask!