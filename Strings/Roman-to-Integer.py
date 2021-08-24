"""
Difficulty: Easy

Directions: Convert Roman numerals to corresponding base 10 integer

Example: IV = 4, MCMXCIV = 1994

Constraints: numeral <= 3999
"""

def romanToInt(self, s: str) -> int:
    mapped = {"I":1,
                "IV":4,
                "IX":9,
                "V":5,
                "X":10,
                "XL":40,
                "XC":90,
                "C":100,
                "CD":400,
                "CM":900,
                "D":500,
                "L":50,
                "M":1000
    }
    value = ii = 0
    while ii < len(s):
        if ii < len(s)-1 and s[ii]+s[ii+1] in mapped:
            value += mapped[s[ii]+s[ii+1]]
            ii += 2
        else:
            value += mapped[s[ii]]
            ii += 1
            
    return value