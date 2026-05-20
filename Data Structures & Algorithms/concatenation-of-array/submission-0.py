class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=len(nums)
        return [nums[i%k] for i in range(2*k) ]