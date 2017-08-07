class Solution:
    # @param A: An integers list.
    # @return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] > A[mid-1]:
                start = mid
            elif A[mid] > A[mid+1]:
                end = mid
            else:
                # 当mid在谷底时，可以将其变为start, 也可以用end
                start = mid

        if A[start] > A[start-1] and A[start] > A[start+1]:
            return start
        return end