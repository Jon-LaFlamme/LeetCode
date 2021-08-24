"""
Difficulty: Easy

Directions: Given a 32-bit signed integer, reverse the decimal representation of that numbner

Example: 123 = 321

Constraints: -(2**31) > ans < (2**31 -1)
"""

# Originally misunderstood the problem as a bit manipulation problem
# Subsequently solved after reviewing solutions and implementing based on string reversal idea
def reverse(self, x: int) -> int:
        
    sign = -1 if x < 0 else 1

    rev = int(str(abs(x))[::-1])*sign
    if rev > (2**31-1) or rev < -(2**31):
        return 0
    else:
        return rev