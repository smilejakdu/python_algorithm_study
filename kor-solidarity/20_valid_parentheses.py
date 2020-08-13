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

# print(Solution().isValid("([)]"))
# print(Solution().isValid("{[]}"))
