"""
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

"""

# Initial Brute Force with Memoization. Failed on very large test cases (time limit exceeded)
def superpalindromesInRange(self, left: str, right: str) -> int:
    
    def is_palindrome(x):       # Checks if x is a palindrome
        j = 0
        k = len(x)-1
        while j <= k:
            if x[j] == x[k]:
                j += 1
                k -= 1
            else:
                return False
        return True
    
    # cases: 1) is_p==False 2) is_p==True 3) is_p==?
    pals = set()
    not_pals = set()
    ct = 0
    
    #Does ii have a perfect square?
        # Then check if ii and sqrt(ii) are palindromes. store outcomes in sets
    
    
    for ii in range(int(left), int(right)+1):
        ii = str(ii)
        sqrt = math.sqrt(int(ii))         
        if sqrt % 1 == 0:
            sqrt = str(int(sqrt))
            if sqrt in pals:
                if is_palindrome(ii):
                    pals.add(ii)
                    ct +=1
                else:
                    not_pals.add(ii) 
            elif sqrt not in not_pals:      
                if is_palindrome(ii):
                    pals.add(ii)
                    if is_palindrome(sqrt):
                        ct += 1  
                else:
                    not_pals.add(ii)
                                        
    return ct

# Below is my attempt to optimize the algorithm
def superpalindromesInRange(self, left: str, right: str) -> int:
    
    
    def is_palindrome(x):       # Checks if x is a palindrome
        j = 0
        k = len(x)-1
        while j <= k:
            if x[j] == x[k]:
                j += 1
                k -= 1
            else:
                return False
        return True
    
    # cases: 1) is_p==False 2) is_p==True 3) is_p==?
    #pals = set()
    #not_pals = set()
    ct = 0
    
    #num = 0


    for ii in range(int(math.sqrt(int(left))), int(math.sqrt(int(right)))+1):
        #num += 1
        if not str(bin(ii))[-1]==0:
            if str(ii)[0] == str(ii)[-1]:
                if is_palindrome(str(ii)):
                    #if ii**2 in pals:
                    #ct += 1   
                    if str(ii**2)[0] == str(ii**2)[-1]:                  
                        if is_palindrome(str(ii**2)):
                            #pals.add(ii**2)
                            ct += 1
    #print(num)

        
                                        
    return ct