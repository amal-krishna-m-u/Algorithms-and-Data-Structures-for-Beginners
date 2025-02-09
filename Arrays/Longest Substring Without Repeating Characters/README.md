# Longest Substring Without Repeating Characters – Detailed Explanation

This code snippet solves the problem of finding the length of the longest substring in a given string `s` that does not contain any repeating characters. For the example `s = "pwwkew"`, the expected output is `3` (the substring `"wke"` is one such longest substring).

---

## Code Listing

```python
s = "pwwkew"
# Expected output: 3

def lengthOfLongestSubstring(s) -> int:
    # If the string has less than 2 characters, return its length
    if len(s) < 2:
        return len(s)
    
    character = set()          # Set to store unique characters in the current window
    left = 0                   # Left pointer of the sliding window
    right = 0                  # Right pointer of the sliding window
    max_len = float('-inf')    # Initialize maximum length to negative infinity
    
    # Iterate with the right pointer over the string
    while right < len(s):
        # If the current character is already in the set, there is a repetition
        if s[right] in character:
            # Move the left pointer rightward until the repeating character is removed
            while s[right] != s[left]:
                character.remove(s[left])
                left += 1
            # Remove the repeated character at the left pointer and move left pointer once more
            character.remove(s[left])
            left += 1
        
        # Update the maximum length with the current window size
        max_len = max(max_len, right - left + 1)
        
        # Add the current character to the set and move the right pointer forward
        character.add(s[right])
        right += 1
    
    return max_len

print("output:", lengthOfLongestSubstring(s))
```

---

## Detailed Explanation

### 1. Problem Overview

- **Objective:**  
  Determine the length of the longest substring without any repeating characters.
  
- **Example:**  
  For the input `s = "pwwkew"`, one of the longest substrings without repeating characters is `"wke"`, which has a length of `3`.

### 2. Key Variables and Initialization

- **`character` (set):**  
  Used to keep track of the unique characters in the current sliding window.
  
- **Pointers:**  
  - `left`: Marks the start of the current window.  
  - `right`: Marks the end of the current window.
  
- **`max_len`:**  
  Holds the maximum length of a valid substring found so far. It is initialized to negative infinity to ensure any valid window will be larger.

### 3. The Sliding Window Technique

The sliding window approach is used to expand and contract a window over the string such that it always contains unique characters.

1. **Expanding the Window:**
   - The `right` pointer moves across the string, adding the current character to the set.
   - **Before Adding:**  
     If the character at `s[right]` is already in the set, a duplicate is encountered.

2. **Handling Duplicates:**
   - When a duplicate is found (`s[right] in character`), the code enters a `while` loop.
   - **Inside the Loop:**
     - The loop removes characters from the left side of the window until the duplicate character (matching `s[right]`) is removed.
     - This is done by:
       - Removing `s[left]` from the set.
       - Incrementing the `left` pointer to narrow the window.
   - After the inner loop, the duplicate character is removed and the `left` pointer is moved one extra step to ensure the window no longer contains the duplicate.

3. **Updating the Maximum Length:**
   - After ensuring that the current window has all unique characters, the window size is calculated as `right - left + 1`.
   - The `max_len` is updated using the `max()` function to store the largest window size encountered.

4. **Final Result:**
   - The loop continues until the `right` pointer has processed all characters.
   - Finally, `max_len` is returned, which represents the length of the longest substring without repeating characters.

### 4. Edge Cases

- **Short Strings:**  
  If the string length is less than 2, the function immediately returns the string's length since any string with 0 or 1 character is unique by default.

---

## Other Important Info

### Inbuilt Functions and Concepts

- **`set` Data Structure:**
  - **Purpose:**  
    A set stores unique items and provides O(1) average time complexity for membership checks.
  - **Use Case:**  
    It is used to quickly determine whether a character is already present in the current substring.

- **Sliding Window Technique:**
  - **Concept:**  
    This technique involves using two pointers to create a window over the data and dynamically adjusting the window size based on certain conditions (in this case, uniqueness of characters).
  - **Benefits:**  
    It efficiently handles problems that require checking contiguous subarrays or substrings, reducing the need for nested loops.

- **`max()` Function:**
  - **Purpose:**  
    Returns the maximum of the provided arguments.
  - **Use Case:**  
    Updates `max_len` by comparing the current window size with the maximum size found so far.

- **While Loop:**
  - **Purpose:**  
    Continuously removes characters from the left until the duplicate is removed.
  - **Benefit:**  
    Ensures the current window always satisfies the condition of having unique characters.

This explanation should help you understand how the sliding window technique is applied to solve the problem and why each step is necessary. If you have further questions or need additional clarification, feel free to ask!