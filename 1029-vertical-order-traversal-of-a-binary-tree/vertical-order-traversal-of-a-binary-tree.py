# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store {column: {row: min-heap of node values}}
        node_map = defaultdict(lambda: defaultdict(list))

        # Queue for BFS traversal (stores node and its (column, row))
        queue = deque([(root, 0, 0)])

        while queue:
            node, col, row = queue.popleft()
            heapq.heappush(node_map[col][row], node.val)

            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        # Extract results in sorted order
        result = []
        for col in sorted(node_map.keys()):
            column_nodes = []
            for row in sorted(node_map[col].keys()):
                while node_map[col][row]:
                    column_nodes.append(heapq.heappop(node_map[col][row]))
            result.append(column_nodes)

        return result