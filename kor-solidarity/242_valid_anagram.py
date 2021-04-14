# Runtime: 48 ms, faster than 58.85% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 32.20% of Python3 online submissions for Valid Anagram.

# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 받아오는 두 스트링이 아나그램인지 확인하기.

        # 기본적으로 두 스트링이 같은 수의 글자를 가지고 있는지 확인해보면 된다.

        # 빈칸 전부 제거 후 소문자 처리
        # s = sorted(s.replace(' ', '').lower())
        # t = sorted(t.replace(' ', '').lower())
        # return bool(s == t)

        # 위 방법도 가능한데... 한번 좀 더 세분화시켜보는걸로.

        # 빈칸 전부 제거 후 소문자 처리
        s = s.replace(' ', '').lower()
        t = t.replace(' ', '').lower()
        # 길이가 안맞으면 거짓
        if len(s) != len(t):
            return False
        # 각 글자의 수가 맞는지 대조
        counter = {}
        for letter in s:
            # 카운터 안에 글자가 있으면 1 증가
            if letter in counter:
                counter[letter] += 1
            # 없다면 처음 등장하는 글자기 때문에 새로 등록
            else:
                counter[letter] = 1
        # t 를 돌릴때는 역으로 감소시킨다.
        for letter in t:
            if letter in counter:
                counter[letter] -= 1
            # 걸리면 애초에 서로 다른 글자가 있다는 뜻이므로 여기서 끝
            else:
                return False
        for i in counter:
            # 최종적으로 모든 값이 0이 돼야한다.
            if counter[i] != 0:
                return False
        return True
