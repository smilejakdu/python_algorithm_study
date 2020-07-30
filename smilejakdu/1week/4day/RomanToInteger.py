''':arg


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

II+ IX = 11
2 + 9 = 11

IIIX


'''
''':arg
Input: "IV"
5 -1 = 4
Output: 4

Input: "IX"
10 -1 = 9
Output: 9

Input : "XL"
50-10 = 40
Output : 40

Input : "XC"
100-10 = 90
Output : 90

Input : "CM"
1000-100 = 900
Output: 900

Input : "CD"
500-100 = 400
Output: 400

'''

''':arg
method 1 
'''
Input = "MCMXCIV"

numbers = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


class Solution(object):
    def romanToInt(self, s):

        if not s:
            return 0
        if numbers.get(s[:2]):
            return numbers.get(s[:2]) + self.romanToInt(s[2:])
        return numbers.get(s[:1]) + self.romanToInt(s[1:])


s = Solution()
print(s.romanToInt(Input))
