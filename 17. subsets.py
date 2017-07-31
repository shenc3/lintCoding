# 递归三要素
# 1. 递归的定义：在 Nums 中找到所有以 subset 开头的的集合，并放到 results

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def helper(self, subset, nums, startIndex):
        self.results.append(subset[:])
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.helper(subset, nums, i+1)
            subset.pop()

    def subsets(self, S):
        # write your code here
        self.results = []
        if S is None:
            return self.results

        if len(S) == 0:
            self.results.append([])
            return self.results

        S.sort()
        self.helper(list(), S, 0)
        return self.results

'''
s = Solution()
s.subsets([1,2,3])
'''

class Solution:
    
    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return
        print(S + [nums[index]])
        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)
        
    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
