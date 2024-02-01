"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        dict = {}
        i,j = 0,0
        n = len(s)
        while(j < n):
            c = s[j]               
            dict[c] = 1 if not c in dict else dict[c] - 1                      
            if dict[c] < 1:
                while(dict[c] < 1):
                    dict[s[i]] += 1
                    i += 1                    
            maxLength = max(maxLength, j - i + 1)
            j += 1
            return maxLength
