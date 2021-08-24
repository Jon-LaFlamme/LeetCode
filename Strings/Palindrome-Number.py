"""
Difficulty: Easy

Directions: Given an integer x return True if x is a palindrome

Examples: 121 = True, -121 = False
"""

# Int -> Str -> List iteration comparisons
def isPalindrome(self, x: int) -> bool:
    
    if x < 0:
        return False
    
    x = str(x)
    is_even = len(x) % 2 == 0

    ii = 0
    jj = 0
    if is_even:
        jj = len(x) // 2
        ii = jj-1
    else:
        jj = len(x) // 2
        ii = jj
    
    while ii >= 0:
        if x[ii] != x[jj]:
            return False
        ii -= 1
        jj += 1
    
    return True

## Better solution, taken from @navinmittal29
def isPalindrome(self, x: int) -> bool:
	if x < 0:
		return False
	
	return str(x) == str(x)[::-1]