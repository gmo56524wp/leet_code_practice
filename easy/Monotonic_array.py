class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mono_incre = False
        mono_decre = False
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                mono_decre = True
            elif nums[i] > nums[i-1]:
                mono_incre = True
        if mono_incre and not mono_decre:
            return True
        elif mono_decre and not mono_incre:
            return True
        elif not mono_decre and not mono_incre:
            return True
        else:
            return False