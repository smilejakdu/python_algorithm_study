# 미완성
class Solution:
    def countAndSay(self, n: int) -> str:
        str_n = str(n)
        counter = 0
        older = None
        current = None
        output = ''
        for i in str_n:
            if current != i:
                # if older:
                    # for i in older:

                current = i
            elif current == i:
                counter += 0




Solution().countAndSay(11)