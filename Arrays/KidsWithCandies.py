"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
"""

#Concise one-liner
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_c = max(candies)
    return [True if x+extraCandies>=max_c else False for x in candies]

#Note: Others more performant by computing a threshhold from and comparing to that through iteration
#ie. thresh = max(candies) - extraCandies
#then: [x >= thresh for x in candies]