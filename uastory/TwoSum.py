from itertools import permutations


class Solution:

    def twoSum(self, nums, target):
        for index, v in enumerate(nums):
            fv = target - v
            try:
                r_index = nums.index(fv, index+1)
                if r_index:
                    return [index, r_index]
            except ValueError:
                pass
        raise Exception('failed')

    def _twoSum(self, nums, target):
        for case in set(permutations(nums, 2)):
            if target == sum(case):
                a1, a2 = case
                if a1 == a2:
                    a1_index = nums.index(a1)
                    a2_index = nums.index(a2, a1_index+1)
                    return [a1_index, a2_index]
                else:
                    return [nums.index(a1), nums.index(a2)]
        raise Exception('failed')


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        [[2, 7, 11, 15], 9, [0, 1]],
        [[3, 3], 6, [0, 1]],
        [[3, 2, 4], 6, [1, 2]],
    ]
    for nums, target, expected in test_cases:
        if expected == solution.twoSum(nums, target):
            print('success')
        else:
            print(
                    'failed...',
                    nums, target, expected,
                    solution.twoSum(nums, target))
