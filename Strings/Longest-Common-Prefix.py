"""
Difficulty: Easy

Directions: Return the Longest Common Prefix 
            for all strings in an array of strings
Examples: 
            Input: strs = ["flower","flow","flight"]
            Output: "fl"
"""

# Solution Came pretty easy for this one.
def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ""
    first = strs[0]
    ii = 0
    
    while True:
        for item in strs:
            if len(item) == ii or item[ii] != first[ii]:
                return prefix
        ii += 1
        prefix = first[:ii]
    return prefix