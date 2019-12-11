# coding=utf-8
class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        else:
            i, j = 0, 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    del nums[j]
                    continue
                else:
                    i += 1
                    j += 1
            return len(nums)


if __name__ == '__main__':
    test_list = [[1, 1, 2], [1, 1, 2, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for l in test_list:
        solution = Solution
        print(solution.removeDuplicates(l))
