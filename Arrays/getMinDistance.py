"""
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
"""
import math

#Brute Force Solution O(n):
def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    nearest = math.inf
    for ii in range(len(nums)):
        if nums[ii] == target:
            if abs(start - ii) < nearest:
                nearest = abs(start - ii)
    return nearest

#Optimized still O(n) but likely faster in avg case:
def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    nearest = math.inf
    n = len(nums)
    if nums[start] == target:
        return 0

    ii = start
    jj = start
    while jj < n-1 or ii > 0:
        ii -= 1
        jj += 1
        if jj <= n-1:
            if nums[jj] == target:
                return abs(start-jj)
            
        if ii >= 0:
            if nums[ii] == target:
                return abs(start-ii)