# Runtime: 20 ms, faster than 98.92% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.7 MB, less than 94.86% of Python3 online submissions for Length of Last Word.

# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 받은 스트링의 마지막 단어의 길이를 구하라는 질문.

        # 단어가 아예 없는 경우 0
        if not s.split():
            return 0
        # 그게 아닌 경우 쪼개서 나온 마지막 단어의 길이를 반환
        return len(s.split()[-1])
