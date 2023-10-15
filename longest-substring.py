"""
question Given a string s, find the length of the longest substring 
without repeating characters.
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = 0   # This variable represents the starting index of the current substring.
        k = 0   # This variable represents the ending index of the current substring.
        m = {}  # This dictionary (map) is used to store the last seen index of each character.
        result = 0  # This variable will store the length of the longest substring found.

        while k < len(s):
            if s[k] not in m or v > m[s[k]]:
                # If the character at index k is not in the dictionary 'm', or
                # if the last seen index of the character is less than the current starting index 'v',
                # it means the character is not repeating in the current substring.
                # In this case, update 'result' with the maximum length found so far.
                result = max(result, (k - v + 1))
                m[s[k]] = k  # Update the last seen index of the character.
            else:
                # If the character is repeating in the current substring, we need to adjust 'v'.
                # We set 'v' to be one index after the last seen index of the repeating character,
                # and then update 'result' accordingly.
                v = m[s[k]] + 1
                result = max(result, (k - v + 1))
                k -= 1  # Move 'k' back one step to continue processing from the adjusted 'v'.
            k += 1  # Move 'k' to the next character in 's'.

        return result  # Return the length of the longest substring without repeating characters.

#used sliding window to solve this problem