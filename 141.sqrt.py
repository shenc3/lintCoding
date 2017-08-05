class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        
        index = 1
        while index * index < x:
            index *= 10

        nums = range(index+1)
        start, end = 0, len(nums) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] * nums[mid] < x:
                start = mid
            else:
                end = mid

        if nums[end] * nums[end] == x:
            return nums[end]
        else:
            return nums[start]
