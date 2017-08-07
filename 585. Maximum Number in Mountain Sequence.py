class Solution:
    # @param {int[]} nums a mountain sequence
    #                which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid-1]:
                start = mid
            elif nums[mid] < nums[mid-1]:
                end = mid
            else:
                start = mid
                
        # start一定是峰值吗
        return nums[start]
