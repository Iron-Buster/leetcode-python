# 2476. 二叉搜索树最近节点查询
# 第 320 场周赛
# Q2
# 1597
# 相关标签
# 相关企业
# 提示
# 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

# 请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

# mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
# maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
# 返回数组 answer 。
# Definition for a binary tree node.

from bisect import *
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        a = []
        def dfs(o: Optional[TreeNode]) -> None:
            if o is None: return
            dfs(o.left)
            a.append(o.val)
            dfs(o.right)
        dfs(root)
        ans = []
        for q in queries:
            l = bisect_right(a, q)
            mn = a[l - 1] if l else -1
            r = bisect_left(a, q)
            mx = a[r] if r < len(a) else -1
            ans.append([mn, mx])
        return ans