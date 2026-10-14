class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hide = nums[0]
        seek = nums[0]

        while True:
            hide = nums[hide]
            seek = nums[nums[seek]]
            if hide == seek:
                break
        hide = nums[0]
        while hide != seek:
            hide = nums[hide]
            seek = nums[seek]
        return seek