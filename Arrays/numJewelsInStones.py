"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

# ~3 min to find optimal solution at O(n)
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    j = {}
    ct = 0
    for c in jewels:
        j.update({c:0})
    for s in stones:
        if s in j:
            ct += 1
    return ct
