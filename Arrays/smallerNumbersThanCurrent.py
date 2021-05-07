"""
Runtime: 56 ms, faster than 77.34% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 14.4 MB, less than 13.73% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
"""


# Took about ~29 min to find more optimal solution at O(n log n)
# Brute force would have been O(n^2). I skipped brute force entirely
# Utilizes dictionary to store the indices for each unique number
# Heapsorts the list achieve a sorted list
# There were even better solutions. One coder achieved linear time!

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    index = {}
    res = []
    for ii in range(len(nums)):
        nums[ii] *= -1
        res.append(0)
    
    for ii in range(len(nums)):
        if nums[ii] in index:
            lst = index[nums[ii]]
            lst.append(ii)
            index[nums[ii]] = lst
        else:
            index.update({nums[ii]:[ii]})            
    print(index)
    heapq.heapify(nums)
    prior = heapq.heappop(nums)
    while len(nums) > 0:
        if nums[0]==prior:
            prior = heapq.heappop(nums)
        else:
            lst = index[prior]
            for loc in lst:
                res[loc] = len(nums)
            prior = heapq.heappop(nums)
    return res