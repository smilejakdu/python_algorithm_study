class Solution:
    def romanToInt(self, s: str) -> int:
        cloned = s
        roman_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        # 우선 숫자별로 하나씩.
        # 큰 단위부터 하나하나.
        answer = 0
        # 하나 남을때까지.
        while len(cloned) > 1:
            front_num = 0
            m = cloned.find('M')
            # 0보다 크다면 앞에 뭔가가 있고 뺄게 존재한다는거. 그리고 이 경우는 하나뿐이다.
            # C 가 붙은거. 확인할 필요도 없음.
            if 0 < m:
                answer += 900
                cloned = cloned[m + 1:]
                continue
            # 없다면 M은 추가할 게 없다. 천 추가하고 끝
            elif m == 0:
                answer += 1000
                cloned = cloned[1:]
                continue

            # 다음은 D
            d = cloned.find('D')
            # D 가 1 이상이면 이 또한 볼거없이 앞에 C임.
            if 0 < d:
                answer += 400
                cloned = cloned[d + 1:]
                continue
            # 이 경우 두가지가 존재. D 혼자거나 앞에 뭐가 있거나. 근데 앞에 있을땐 C 만 찾으면 됨
            elif d == 0:
                # 앞에 C 는 최대 3까지 가능
                while front_num < 3:
                    if len(cloned) < front_num and cloned[front_num + 1] == 'C':
                        front_num += 1
                    else:
                        break
                answer += 500 + (front_num * 100)
                cloned = cloned[1 + front_num:]
                continue

            # 나머지 위와 똑같은 식으로 V까지 간다.
            c = cloned.find('C')
            if 0 < c:
                answer += 90
                cloned = cloned[c + 1:]
                continue
            elif c == 0:
                answer += 100
                cloned = cloned[1:]
                continue

            l = cloned.find('L')
            if 0 < l:
                answer += 40
                cloned = cloned[l+1:]
                continue
            elif l == 0:
                while front_num < 3:
                    if len(cloned) < front_num and cloned[front_num + 1] == 'X':
                        front_num += 1
                    else:
                        break
                answer += 50 + (front_num * 10)
                cloned = cloned[1 + front_num:]
                continue

            x = cloned.find('X')
            if 0 < x:
                answer += 9
                cloned = cloned[x+1:]
                continue
            elif x == 0:
                answer += 10
                cloned = cloned[1:]
                continue

            v = cloned.find('V')
            if 0 < v:
                answer += 4
                cloned = cloned[v+1:]
                continue
            elif v == 0:
                while front_num < 3:
                    if len(cloned) < front_num and cloned[front_num + 1] == 'I':
                        front_num += 1
                    else:
                        break
                answer += 5 + (front_num * 1)
                cloned = cloned[front_num + 1:]
                continue

            i = cloned.find('I')
            # 마지막에 I는 그냥 1이란거...
            if i == 0:
                answer += 1
                cloned = cloned[1:]
                continue

        # last one
        if len(cloned):
            answer += roman_num.get(cloned)
        return answer
