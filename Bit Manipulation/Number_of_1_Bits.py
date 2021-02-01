"""
Difficulty: Very Easy

Directons: Given an integer, return the number of 1's present in the integer's binary form:
"""
def hammingWeight(n: int) -> int:
    return int(bin(n).count("1"))

    """Summary Useful Functions:
    bin(int) -> returns the binary form of an integer
    str_obj.count("str_arg") -> int: number of occurences of "str_arg" in str_obj
    """


if __name__ == "__main__":
    print(hammingWeight(3567))
    print(hammingWeight(3))
    print(hammingWeight(1))
    print(hammingWeight(2))
    print(hammingWeight(7))
    print(hammingWeight(0))
