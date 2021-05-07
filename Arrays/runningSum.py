"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

#Solution scored in the 99th percentile
def runningSum(self, nums: List[int]) -> List[int]:
    for ii in range(1, len(nums)):
        nums[ii] += nums[ii-1]
    return nums