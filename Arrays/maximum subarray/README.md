# Maximum Subarray – Detailed Explanation

This code snippet solves the **Maximum Subarray Problem**, where the goal is to find the contiguous subarray within a one-dimensional array of numbers which has the largest sum. The algorithm used here is a form of **Kadane's Algorithm**, which efficiently finds the maximum sum in O(n) time.

---

## Code Listing

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Expected output: 6

def maxSubArray(nums):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity to handle all negative numbers
    curr_sum = 0             # Start current sum at 0
    
    for num in nums:
        # If curr_sum is negative, reset it to 0 before adding the current number.
        curr_sum = max(curr_sum, 0) + num
        
        # Update max_sum if the current sum is larger than the max_sum found so far.
        max_sum = max(curr_sum, max_sum)
    
    return max_sum
        
print(maxSubArray(nums))
```

---

## Detailed Explanation

### Overview

- **Input:**  
  An array of integers, for example: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`.
- **Output:**  
  The function returns the maximum sum of any contiguous subarray. In this example, the maximum subarray sum is `6`, which corresponds to the subarray `[4, -1, 2, 1]`.

### Step-by-Step Process

1. **Initialization:**
   - **`max_sum` is set to `float('-inf')`:**  
     This ensures that any sum encountered in the array, including all negative sums, will be larger than the initial value.
   - **`curr_sum` is set to `0`:**  
     This variable keeps track of the sum of the current subarray being evaluated.

2. **Iteration Over the Array:**
   - The code uses a `for` loop to iterate over each number in the list.
   - **Resetting Negative Sums:**  
     The expression `max(curr_sum, 0)` ensures that if `curr_sum` is negative, it resets to `0` before adding the current number. This is a key step because a negative sum would only decrease the total when added to subsequent numbers.
   - **Updating `curr_sum`:**  
     Each number is added to the current sum after potentially resetting it:
     ```python
     curr_sum = max(curr_sum, 0) + num
     ```
   - **Updating `max_sum`:**  
     After updating `curr_sum`, the algorithm compares it with `max_sum`:
     ```python
     max_sum = max(curr_sum, max_sum)
     ```
     If `curr_sum` is larger than the current `max_sum`, it becomes the new maximum.

3. **Return Value:**
   - After iterating through the entire array, `max_sum` holds the maximum sum of any contiguous subarray, which is then returned by the function.

---

## Other Important Info

### Inbuilt Functions and Concepts

- **`float('-inf')`:**
  - **Purpose:**  
    Represents negative infinity, ensuring that any real number will be larger. This is used to initialize `max_sum` so that it can properly handle arrays with negative values.
  - **Use Case:**  
    Prevents incorrect results when all numbers in the array are negative.

- **`max()` Function:**
  - **Purpose:**  
    Returns the maximum of the given arguments.
  - **Use Cases in This Code:**  
    - `max(curr_sum, 0)`: Ensures that `curr_sum` is not negative before adding the next number.
    - `max(curr_sum, max_sum)`: Updates the running maximum sum.
  - **Benefit:**  
    Simplifies the logic by neatly handling comparisons and ensuring the algorithm resets or updates sums correctly.

- **Kadane's Algorithm:**
  - **Concept:**  
    An efficient algorithm to solve the Maximum Subarray Problem by maintaining a running sum (`curr_sum`) and updating the maximum found so far (`max_sum`).
  - **Advantage:**  
    Runs in linear time (O(n)), making it highly efficient for large arrays.

- **For Loop:**
  - **Purpose:**  
    Iterates through each element of the list.
  - **Role in This Code:**  
    Allows the algorithm to process each number one by one and update the current and maximum sums accordingly.

This detailed explanation should help you understand not only how the algorithm works but also why each step is necessary. The use of built-in functions and resetting strategies in Kadane's algorithm makes it an elegant and efficient solution to the Maximum Subarray Problem. If you have further questions or need additional clarification, feel free to ask!