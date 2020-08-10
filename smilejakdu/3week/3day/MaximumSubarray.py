''':arg
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

''':arg
    maxcurr = nums[0] 
    maxglobal = nums[0]
    
    우선적으로 index 0 에 대한 값을 넣는다 .
    
    반복문을 1부터 돌린다. 
    max 함수를 이용해서 , nums[i] 와 , maxcurr + nums[i] 의 값을 비교한다 .
    큰 값을 다시 maxcurr 변수에 넣는다.
   
    maxcurr 변수와 maxglobal 변수를 비교한다.  
'''


def maxSubArray(nums):
    maxcurr = nums[0]
    maxglobal = nums[0]
    for i in range(1, len(nums)):
        maxcurr = max(nums[i], maxcurr + nums[i])
        maxglobal = max(maxcurr, maxglobal)
    return maxglobal


print(maxSubArray(nums))
