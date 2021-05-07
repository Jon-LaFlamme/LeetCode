"""
Runtime: 32 ms, faster than 49.74% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 14.2 MB, less than 71.20% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""

# 6 min to solve. O(n) time complexity and O(n) space complexity
def subtractProductAndSum(self, n: int) -> int:
    k = [int(x) for x in ",".join(str(n)).split(",")]
    return math.prod(k) - sum(k)

# Other's approaches:
# Map function to list of integers, then reduce while multiplying.
# Divmod function to iterate backwards through the digits in the number
# 