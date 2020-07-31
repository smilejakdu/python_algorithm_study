''':arg

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

Input = ["flower", "flow", "flight"]


def longestCommonPrefix(strs):
    result = []

    for s in zip(*strs):
        if len(set(s)) != 1:
            return ''.join(result)
        result.append(s[0])
    string = ''.join(result)
    return string


print(longestCommonPrefix(Input))
