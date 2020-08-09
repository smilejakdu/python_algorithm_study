''':arg
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''

nums = [1, 3, 5, 6]
target = 5


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)

    nums.append(target)
    nums.sort()
    return nums.index(target)


''':arg
other answer

끝에 return len(nums) 가 왜 있는지 몰라서 한번 돌려봤다.

그런데 만약에 , 
Input: [1,3,5,6], 7
Output: 4
이처럼 4가 출력 되어야하지만 , 마지막에 return len(nums) 가 없다면 , None 을 출력하게 된다.

'''


def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target or nums[i] > target:
            return i
    return len(nums)
