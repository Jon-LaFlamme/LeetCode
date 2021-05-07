"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""

#Brute Force Solution O(n^2)
def numIdenticalPairs(self, nums: List[int]) -> int:
    pairs = 0
    for bb in range(len(nums)-1, 0, -1):
        for ff in range(bb):
            if nums[bb]==nums[ff]:
                pairs += 1
    return pairs

#Notes: Others solved using a dictionary to store occurences of each integer.
#Then it is only a matter of calculating the number of pairs for a given frequency
#This enhanced solution runs in only O(n) time

