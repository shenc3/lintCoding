class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        # Write your code here
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if target - A[start] < A[end] - target:
            return start
        elif target - A[start] >= A[end] - target:
            return end
        else:
            pass
