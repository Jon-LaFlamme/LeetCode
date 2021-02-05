"""Failed on timeout threshold; otherwise correct."""


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        LHS = 0
        smallest = min(nums)
        greatest = max(nums)
        ii = smallest+1
        while ii <= greatest:

            if ii in nums and ii-1 in nums:
                subseq = list(filter(lambda x: x==ii or x==ii-1, nums))
                if len(subseq) > LHS:
                    LHS = len(subseq)
            ii+=1
        return LHS


"""Another solution on the community:
Gains efficiency by iterating only once through the entire array and storing in dict.



from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        
        for num in nums:
            count[num]+=1                               
        
        LHS = 0
        
        for num in count:
            if num+1 in count:                              
                LHS = max(LHS, count[num]+count[num+1])    
        
        return LHS                                                       
"""