class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def array_to_tree(arr: list) -> TreeNode | None:
    """将层序遍历数组还原为链表结构的二叉树，None 表示空节点"""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        # 左子节点
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        # 右子节点
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def print_tree(root: TreeNode | None, indent: int = 0, label: str = "root"):
    """旋转 90° 的树形结构图"""
    if root is None:
        return
    print_tree(root.right, indent + 4, "R")
    print(" " * indent + f"--{label}:{root.val}")
    print_tree(root.left, indent + 4, "L")


if __name__ == "__main__":
    arr = [10, 5, 15, 3, 7, None, 20]
    root = array_to_tree(arr)

    print("数组:", arr)
    print("\n二叉树结构 (旋转90°, L=左子树, R=右子树):\n")
    print_tree(root)

    print("\n" + "─" * 40)
    print("树形示意图:")
    print(r"""
        10
       /  \
      5    15
     / \     \
    3   7     20
""")
