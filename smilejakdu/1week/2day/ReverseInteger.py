'''
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Input: 100
Output: 1


Input: -10
Output: -1


Input: 901000
Output: 109
'''


class Solution(object):
    def reverse(self, x):
        result_list = []
        list_index = 0
        if 0 > x:
            number_list = list(str(x))
            minus = number_list.pop(0)
            number_list_reverse = number_list[::-1]
            for n in range(0, len(number_list_reverse)):
                if int(number_list_reverse[n]) != 0:
                    list_index = n
                    break

            for i in range(list_index, len(number_list_reverse)):
                result_list.append(number_list_reverse[i])
            if int(''.join(result_list)) >2147483648:
                return 0

            result_list.insert(0, minus)
            result = ''.join(result_list)

            return result

        elif 0 < x:
            number_list = list(str(x))
            number_list_reverse = number_list[::-1]
            for n in range(0, len(number_list_reverse)):
                if int(number_list_reverse[n]) != 0:
                    list_index = n
                    break

            for i in range(list_index, len(number_list_reverse)):
                result_list.append(number_list_reverse[i])
            result = ''.join(result_list)
            if 2147483648 < int(result):
                return 0
            return result

        elif 0 == x:
            return 0
