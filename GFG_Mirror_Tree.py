class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        if root is None:
            return 
        
        root.left, root.right = root.right, root.left 
        self.mirror(root.left)
        self.mirror(root.right)

Time Complexity : O(n)  n->Number of nodes 
Space Complexity : O(h)  h->Height of the tree (Due to recursive call stack)
Depth of Recursion:
The maximum depth of the recursion is equal to the height of the tree. This is because the deepest recursive call will happen when we reach the leaf node of the longest path from the root.
Best Case: O(log n) for a balanced binary tree
In a balanced tree, the height is logarithmic to the number of nodes.
Worst Case: O(n) for a skewed tree (essentially a linked list)
In a completely unbalanced tree, the height could be equal to the number of nodes.
