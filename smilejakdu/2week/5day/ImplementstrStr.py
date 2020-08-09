''':arg
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
haystack = "mississippi"
needle = "issip"
Output : 4
'''

''':arg
answer 1

index() 함수라는것이 있는줄 몰랐다. 
로직을 골똘히 생각하고있었는데 , index 함수로 이렇게 간단하게 풀릴줄이야...
'''


haystack = "mississippi"
needle   = "issip"

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    elif len(needle) == 0:
        return 0
    else:
        return -1

print(strStr(haystack , needle))


''':arg
answer 2
이 풀이도 깔끔해 보였다. 
haystack의 길이를 구한다 .
needle 의 길이를 구한다.
haystack 의 길이에서 needle 의 길이를 뺀다.
haystack[i:i + needle_length] 로 인해서 haystack 의 index i 부터 i+ needle_length 의 길만큼 찾고
return 으로 i 를 반환한다. 
'''

def strStr(self, haystack, needle):
    haystack_length = len(haystack)
    needle_length = len(needle)
    if haystack == needle:
        return 0
    if haystack_length == 0 and needle_length == 0:
        return 0
    for i in range(0, haystack_length - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            return i
    return -1
