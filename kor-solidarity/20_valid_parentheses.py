class Solution:
    def isValid(self, s: str) -> bool:
        layer1 = ['(', '[', '{']
        layer2 = [')', ']', '}']
        real_layer = []
        for i in s:
            if i in layer1:
                real_layer.append(i)
            elif i in layer2:
                match = layer2.index(i)
                if not len(real_layer) or real_layer[-1] != layer1[match]:
                    return False
                real_layer.pop(-1)
        if len(real_layer):
            return False
        return True
        parentheses = [0, 0, 0]
        overall = 0
        pair = {'(': [0, 1], ')': [0, -1], '[': [1, 1], ']': [1, -1], '{': [2, 1], '}': [2, -1]}
        index = 0
        while 0 <= parentheses[0] and 0 <= parentheses[1] and 0 <= parentheses[2] \
                and index < len(s) and 0 <= overall:
            a = pair[s[index]][0]
            b = pair[s[index]][1]
            parentheses[pair[s[index]][0]] += pair[s[index]][1]
            overall += pair[s[index]][1]
            index += 1
        if parentheses[0] == 0 and parentheses[1] == 0 and parentheses[2] == 0 and overall == 0:
            return True
        return False
        # if len(s) % 2 != 0:
        #     return False
        # middle = len(s) // 2
        # match = True
        # for i in range(middle):
        #     mid_back = s[middle + i]
        #     mid_front = pair[s[middle - i - 1]]
        #     if mid_front != mid_back:
        #         match = False
        # return match


# print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))
