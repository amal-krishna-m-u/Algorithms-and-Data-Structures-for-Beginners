s = "pwwkew"
#expected output : 3


def lengthOfLongestSubstring(s) -> int:
    if len(s)<2:
        return len(s)
    
    character = set()
    left =0
    right=0
    max_len=float('-inf')

    

    while right < len(s):

        if s[right] in character:

            while s[right] != s[left]:
                character.remove(s[left])
                left+=1

            character.remove(s[left])
            left+=1

        max_len=max(max_len,right-left+1)
        character.add(s[right])
        right+=1
    
    return max_len



print("output:",lengthOfLongestSubstring(s))
