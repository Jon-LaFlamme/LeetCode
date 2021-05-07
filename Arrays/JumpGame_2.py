"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.
"""

def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        n = len(nums)
        index = n-1
        
        while index > 0:
            max_jump_loc = 0
            for ii in reversed(range(index+1)):
                if ii + nums[ii] >= index:
                    max_jump_loc = ii
            jumps += 1
            index = max_jump_loc
            #print(index)
        return jumps



"""
Performance Notes:
Faster than 87% of submissions
Less memory than 90% of submissions
"""