# Runtime: 76 ms, faster than 38.34% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 80.42% of Python3 online submissions for Longest Substring Without Repeating Characters.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 가장 긴 중복없이 이어지는 글자의 길이를 찾으라는 질문.

        # 정답이 될 수를 넣을 변수, 그리고 넘길 인덱스번호
        num, i, j = 0, 0, 1

        while i < len(s) and j <= len(s):
            # 중복여부
            overlap = False
            # 확인할 스트링
            target = s[i:j]
            for k in target:
                # 만일 내부에 글자가 하나라도 둘 이상이면 중복이 있다는 소리. 앞 스트링을 빼고 통과.
                if target.count(k) > 1:
                    i += 1
                    overlap = True
                    break
            # 다 돌았으면 중복이 있었는지 확인. 중복이 없었을 경우 num 반영.
            # 단, target 이 num 보다 더 큰 경우에만.
            if not overlap and num < len(target):
                num = len(target)
            # 마지막에는 확인할 스트링 늘리기
            j += 1
        return num
