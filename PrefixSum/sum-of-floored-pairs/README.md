# Sum of Floored Pairs - LeetCode Problem Explanation

## Title & Overview

This code solves the "Sum of Floored Pairs" problem, which involves calculating the sum of floor(nums[i] / nums[j]) for all possible pairs of indices (i, j) in the given array. The goal is to efficiently compute this sum while handling large input arrays and preventing integer overflow.

## Code Listing

```python
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count = defaultdict(int)
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        max_num = max(nums)
        range_num_till_n = [0] * (max_num + 1)

        for i in range(1, max_num + 1):
            range_num_till_n[i] = range_num_till_n[i-1] + count[i]

        sum_of_floored_pairs = 0        

        for num in count:
            k = 1
            while num * k <= max_num:
                start = num * k
                end = min((num * (k+1)) - 1, max_num)
                sum_of_floored_pairs += (range_num_till_n[end] - range_num_till_n[start-1]) * k * count[num]
                sum_of_floored_pairs %= MOD
                k += 1
        
        return sum_of_floored_pairs
```

## Detailed Explanation

The solution uses a smart and efficient approach to solve the problem with the following key steps:

### 1. Frequency Counting
- The first step is to count the frequency of each number in the input array.
- A `defaultdict` is used to efficiently track how many times each number appears.
- This helps optimize later calculations by avoiding repeated computations.

### 2. Prefix Sum Preparation
- Create a `range_num_till_n` array that acts as a prefix sum of number frequencies.
- For each index `i`, `range_num_till_n[i]` represents the total count of numbers less than or equal to `i`.
- This allows for quick range queries to determine the count of numbers in a specific range.

### 3. Pair Sum Calculation
- The core algorithm iterates through unique numbers in the input.
- For each number, it calculates floored division results by using a multiplier `k`.
- The inner `while` loop explores different multiplication ranges.

### 4. Range Calculation Strategy
- `start` represents the beginning of a range where floor division equals `k`.
- `end` is the upper bound of this range, capped at the maximum number.
- The formula `range_num_till_n[end] - range_num_till_n[start-1]` efficiently counts numbers in this range.

### 5. Modulo Arithmetic
- To prevent integer overflow, the result is continuously taken modulo `10^9 + 7`.
- This is a common technique in competitive programming to handle large numbers.

## Other Important Info

### Key Python Concepts Used

1. **defaultdict**
   - From the `collections` module
   - Automatically initializes dictionary values
   - Prevents KeyError when accessing non-existent keys
   - Useful for frequency counting and numeric aggregations

2. **Modulo Operator (`%`)**
   - Used for:
     - Preventing integer overflow
     - Keeping numbers within a specific range
   - Common in algorithm problems involving large numbers
   - Maintains result within constraint of 10^9 + 7

3. **min() Function**
   - Used to cap the `end` range at `max_num`
   - Prevents index out of bounds errors
   - Provides a clean way to set upper limits

4. **List Comprehensions & Initialization**
   - `[0] * (max_num + 1)` creates a pre-initialized list
   - Efficient way to create arrays with default values

### Time and Space Complexity
- Time Complexity: O(N + M * log(M)), where N is array length, M is max number
- Space Complexity: O(M) for storing frequency and prefix sum arrays

## Tips for Learners
- Pay attention to range calculations
- Use prefix sum for efficient range queries
- Always consider modulo for large number calculations
- Frequency counting can simplify many algorithmic problems