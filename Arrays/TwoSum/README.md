# Two Sum Problem – Detailed Explanations and Code Walkthrough

This repository provides two different solutions to the classic **Two Sum** problem, where the goal is to find two numbers in a list that add up to a given target. Each solution is explained step-by-step so that even beginners can understand the underlying techniques and reasoning.

## Table of Contents

- [Overview](#overview)
- [Method 1: Hashmap Approach](#method-1-hashmap-approach)
- [Method 2: Two-Pointer Technique](#method-2-two-pointer-technique)
  - [Why Do We Adjust the Pointers?](#why-do-we-adjust-the-pointers)
- [Other Important Info](#other-important-info)

---

## Overview

In the **Two Sum** problem, you are given:
- A list of numbers (e.g., `[2, 7, 15, 25]` or `[2, 5, 8, 3, 7, 15, 25]`).
- A target sum (e.g., `9`).

Your task is to return the indices of the two numbers that add up to the target. Two common approaches to solve this problem are:
1. **Using a Hashmap (Dictionary)**
2. **Using the Two-Pointer Technique** (after sorting the list)

---

## Method 1: Hashmap Approach

### Code

```python
# input
nums = [2, 7, 15, 25]
target = 9
# expected output: [0,1] or [1,0]

def twoSum(nums, target):
    remaining = {}
    
    # Loop through nums with index and value
    for index, num in enumerate(nums):
        balance = target - num
        
        # Check if the complement (balance) exists in our dictionary
        if balance in remaining:
            return [index, remaining[balance]]
        else:
            remaining[num] = index
    return []

print("Two sum result:", twoSum(nums, target))
```

### Explanation

1. **Dictionary Initialization:**  
   We start by creating an empty dictionary (`remaining`) that will store numbers as keys and their indices as values.

2. **Iteration with `enumerate()`:**  
   The `enumerate()` function is used to loop through the list while keeping track of both the index and the number. This makes it easy to store the index in the dictionary.

3. **Calculating the Balance:**  
   For each number, the code calculates `balance = target - num`. This represents the number needed to reach the target when added to the current number.

4. **Checking for the Complement:**  
   - If the `balance` is already in the dictionary, it means that a previous number can pair with the current number to achieve the target sum. The function then returns the indices of these two numbers.
   - If the `balance` is not found, the current number and its index are added to the dictionary for future reference.

5. **Return Statement:**  
   If no matching pair is found after iterating through the list, the function returns an empty list.

---

## Method 2: Two-Pointer Technique

### Code

```python
# input
nums = [2, 5, 8, 3, 7, 15, 25]
target = 9
# expected output: [0,4] or [4,0]

def twoSum(nums, target) -> list:
    left, right = 0, len(nums) - 1

    # Create a list of pairs [original index, value]
    sorted_nums = [[i, n] for i, n in enumerate(nums)]
    # Sort the list based on the numerical values
    sorted_nums = sorted(sorted_nums, key=lambda x: x[1])
    print(sorted_nums)

    while left < right:
        curr_sum = sorted_nums[left][1] + sorted_nums[right][1]
    
        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [sorted_nums[left][0], sorted_nums[right][0]]
        
    return []
    
print(twoSum(nums, target))
```

### Explanation

1. **Preparing the Data:**
   - We pair each number with its original index using list comprehension to create `sorted_nums` as a list of `[index, value]` pairs.
   - The list is then sorted by the values using the `sorted()` function. This ordering is essential for the two-pointer technique to work.

2. **Initializing Two Pointers:**
   - Two pointers are established: `left` starts at the beginning (smallest value) and `right` at the end (largest value) of the sorted list.

3. **Finding the Target Pair:**
   - **Calculate the Current Sum:**  
     The sum of the numbers at the `left` and `right` pointers is calculated.
   - **Adjusting Pointers:**  
     - **If the current sum is greater than the target:**  
       The right pointer is moved one step to the left.  
       **Why?** In a sorted list, the number at the right pointer is one of the largest. Moving left selects a smaller number, thereby reducing the sum.
     - **If the current sum is less than the target:**  
       The left pointer is moved one step to the right.  
       **Why?** The number at the left pointer is one of the smallest. Moving right selects a larger number, increasing the sum.
     - **If the current sum equals the target:**  
       The function returns the original indices of these numbers from the sorted list.
   
4. **Return Statement:**  
   If no valid pair is found after the loop, the function returns an empty list.

---

### Why Do We Adjust the Pointers?

- **Moving the Right Pointer Left:**  
  In a sorted array, the right pointer is at a large number. If the sum exceeds the target, reducing the right pointer moves us to a smaller number, which decreases the sum.

- **Moving the Left Pointer Right:**  
  Conversely, if the sum is too low, increasing the left pointer moves us to a larger number, thereby increasing the sum.

- **Efficiency:**  
  By adjusting pointers based on the current sum relative to the target, we avoid checking every possible pair, significantly reducing the time complexity.

This method is both efficient and elegant, using the sorted property of the list to quickly converge on the solution.

---

## Other Important Info

### Inbuilt Functions and Concepts

- **`enumerate(iterable)`**
  - **Purpose:** Provides both the index and value when iterating through a list.
  - **Use Case:** Essential for keeping track of original indices while iterating over the list.
  
- **Dictionaries (Hashmaps)**
  - **Purpose:** Stores key-value pairs for fast lookup.
  - **Use Case:** In the hashmap approach, it allows us to check for the complement of each number in constant time.
  - **Attributes:** Average O(1) lookup time, which contributes to the efficiency of the solution.

- **List Comprehension**
  - **Purpose:** A concise way to create lists.
  - **Use Case:** Used in the two-pointer method to create a list of pairs that include the original indices.
  
- **`sorted(iterable, key=...)` Function**
  - **Purpose:** Returns a new sorted list.
  - **Use Case:** Sorting the list of `[index, value]` pairs by value is crucial for the two-pointer technique.
  - **Lambda Function:**  
    - **Syntax:** `lambda x: x[1]`
    - **Use:** Specifies that sorting should be done based on the second element (the actual number) of each pair.

- **Two-Pointer Technique**
  - **Purpose:** An efficient strategy to traverse a sorted list from both ends.
  - **How It Works:**  
    - By moving the pointers inward based on whether the sum is too high or too low, we can quickly zero in on the correct pair.
  - **Benefits:**  
    - Reduces the number of comparisons needed compared to a brute-force approach.
    - Typically operates in O(n) time after sorting, making it a practical solution for large lists.

---

This README should help you understand not only how the code works but also the reasoning behind each step, especially the crucial pointer adjustments in the two-pointer approach.