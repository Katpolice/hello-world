# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if (hello == None):
            return
        
        else: 
            self.left, self.right = (
            self.invertTree(self.right)
            self.invertTree(self.left))
        
def print_TreeNode(self) :
    
    if (self == None):
        return
    
    print_TreeNode(self.left)
    print_TreeNode(self.right)
    
hello = TreeNode(4)
hello.left = TreeNode(7)
hello.right = TreeNode(2)
hello.left.left = TreeNode(9)
hello.left.right = TreeNode(6)
hello.right.left = TreeNode(3)
hello.right.right = TreeNode(1)

print_TreeNode(hello)
print_TreeNode(hello.left)
print_TreeNode(hello.right)
print_TreeNode(hello.left.left)
print_TreeNode(hello.left.right)
print_TreeNode(hello.right.left)
print_TreeNode(hello.right.right) 

# Status: Runtime Error 
# Runtime Error Message:
# Line 17: SyntaxError: invalid syntax
# Last executed input: [4,2,7,1,3,6,9]
# Leetcode link: https://leetcode.com/submissions/detail/347883352/ 
# Note to self: Figure out what went wrong and learn from it.
# Also, I should ask a friend about my answer and how to fix it.
