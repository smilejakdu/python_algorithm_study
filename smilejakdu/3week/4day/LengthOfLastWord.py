''':arg
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

Input: "            "
Output: 0

Input: "   "
Output: 0
'''

# s = "          "

s = "hello jakdu"
''':arg
answer 1 
'''


def lengthOfLastWord(s):
    if not s:
        return 0

    if s.strip() == "":
        return 0

    string = s.split().pop()

    return len(string)


print(lengthOfLastWord(s))

''':arg
answer 2 
'''


def lengthOfLastWord(s):
    s = s.strip()
    if not s:
        return 0
    if " " not in s:
        return len(s)
    cnt = 0
    for i in reversed(s):
        if i != " ":
            cnt += 1
        else:
            return cnt


print(lengthOfLastWord(s))

''':arg
answer 3
'''


def lengthOfLastWord(s):
    # trim the trailing spaces
    p = len(s) - 1
    while p >= 0 and s[p] == ' ':
        p -= 1

    # compute the length of last word
    length = 0
    while p >= 0 and s[p] != ' ':
        p -= 1
        length += 1
    return length


print(lengthOfLastWord(s))
