"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

def shuffle(self, nums: List[int], n: int) -> List[int]:
    res = []
    for ii in range(n):
        res.append(nums[ii])
        res.append(nums[ii+n])
    return res