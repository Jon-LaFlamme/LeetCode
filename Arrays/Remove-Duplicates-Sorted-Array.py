"""
Difficulty: Easy

Directions: Given a sorted integer array, 
    return the number of unique numbers in the array,
    complete this in-place

Constraints -100 >= x
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        value = -101
        index = 0
        for v in nums:
            if v > value:
                nums[index] = v
                index += 1
                value = v
            
        return index