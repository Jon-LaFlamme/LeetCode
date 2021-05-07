"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
"""

# Pretty quickly saw the Longest Common Subsequence Pattern and 
# then implemented it using my Algorithms textbook with some small mods
# The runtime is O(m*n)

def minDistance(self, word1: str, word2: str) -> int:
    a = len(word1)
    b = len(word2)
    
    res = [0]*(a+1)  # used to store lcs res
    for i in range(a+1):
        res[i] = [0]*(b+1)

    # lcs mapping
    for i in range(1, a+1):
        for j in range(1, b+1):
            if word1[i-1] == word2[j-1]:
                res[i][j] = res[i-1][j-1] + 1   
            elif res[i-1][j] >= res[i][j-1]:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = res[i][j-1]

    k = res[a][b]
    return a-k + b-k