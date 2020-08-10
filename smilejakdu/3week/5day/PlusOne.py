''':arg
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

# digits = [9]
digits = [4, 3, 2, 1]

''':arg
answer 1 
'''


def plusOne(digits):
    string = ''.join([str(d) for d in digits])
    to_string = str(int(string) + 1)
    result = []
    for string in to_string:
        result.append(int(string))

    return result


print(plusOne(digits))

''':arg
answer 2 
'''


def plusOne(digits):
    m = ''
    for i in range(len(digits)):
        m += str(digits[i])
    m = int(m)
    m += 1
    res = [int(x) for x in str(m)]
    return res


print(plusOne(digits))
