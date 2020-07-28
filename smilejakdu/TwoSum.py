class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n1 in range(0 , len(nums)):
            for n2 in range(1 , len(nums)):
                if nums[n1]+nums[n2] == target and n1 != n2:
                    return [n1,n2]
