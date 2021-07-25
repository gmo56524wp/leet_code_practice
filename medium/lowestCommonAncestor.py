class Treenode:
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        elif root == p or root == q:
            return root
        else:
            right = self.lowestCommonAncestor(root.righ, p, q)
            left = self.lowestCommonAncestor(root.left, p, q)
            if right != None and left != None:
                return root
            elif right != None and left == None:
                return right
            else:
                return left