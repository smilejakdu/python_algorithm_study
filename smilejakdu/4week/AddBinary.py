''':arg

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

''':arg
answer 1 

1. 우선 바이너리 부분을 10 진수로 바꾼다 
2. 10진수로 바꾼 뒤 int 로 바꿔서 두수를 더한다.
3. 더한값을 다시 바이너리로 바꾼다.

'''

a = "11"
b = "1"


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a_int = int(a, 2)
    b_int = int(b, 2)
    result = a_int + b_int
    result_bin = "{0:b}".format(result)

    return result_bin


print(addBinary(a, b))
