#MY CODE FOR THIS PROBLEM: https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        

        int right_tree = maxDepth(root.right) + 1;
        int left_tree = maxDepth(root.left)+1;
        if (right_tree> left_tree){
            return right_tree;
        }
        else{
            return left_tree;
        }
    }
}
