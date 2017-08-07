class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    """
    #1. mid和target的位置关系分为在同一个区间和不在同一区间，
            然后考虑大小关系，确定start和end的迭代方向
    #2. 考虑边界情况，所以把target > A[0] 和 target < A[-1]改为
            target >= A[0] 和 target <= A[-1]
    """
    
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if (A[mid] > A[0] and target >= A[0]) or\
            (A[mid] < A[-1] and target <= A[-1]):
                if A[mid] < target:
                    start = mid
                else:
                    end = mid
            else:
                if A[mid] > target:
                    start = mid
                else:
                    end = mid
                
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1