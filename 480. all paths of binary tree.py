# 为何一定要一个DFS辅助函数

class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        self.res = []
        if not root:
            return self.res
        self.DFS(self.res, root, str(root.val))
        return self.res

    def DFS(self, res, root, cur):
        if root.left is None and root.right is None:
            res.append(cur)
        if root.left:
            self.DFS(res, root.left, cur+'->'+str(root.left.val))
        if root.right:
            self.DFS(res, root.right, cur+'->'+str(root.right.val))
