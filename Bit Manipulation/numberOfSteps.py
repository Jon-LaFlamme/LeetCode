""""
Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
""""

# Took a somewhat brute force solution to this as follows:
def numberOfSteps(self, num: int) -> int:
    if num == 0:
        return num
    ct = 0
    while num > 0:
        if num % 2 == 1:
            num -= 1
            ct += 1
        else:
            num /= 2
            ct += 1
    return ct

# Another dev came up with a really nice solution in binary using pattern discovery
# He used the number of 1's and zeros in the number to make a single computation wrt the number of ops required.
def numberOfSteps (self, num: int) -> int:
    return bin(num).count("1") * 2 + bin(num).count("0") - 2
#Fing brillinant!