class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst_insert(root: BSTNode | None, val: int) -> BSTNode:
    if root is None:
        return BSTNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root


def find_min(node: BSTNode) -> BSTNode:
    while node.left:
        node = node.left
    return node


def find_max(node: BSTNode) -> BSTNode:
    while node.right:
        node = node.right
    return node


def delete_by_predecessor(root: BSTNode | None, key: int) -> BSTNode | None:
    """删除节点，用中序前驱（左子树最大值）替换"""
    if root is None:
        return None
    if key < root.val:
        root.left = delete_by_predecessor(root.left, key)
    elif key > root.val:
        root.right = delete_by_predecessor(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        pred = find_max(root.left)
        root.val = pred.val
        root.left = delete_by_predecessor(root.left, pred.val)
    return root


def delete_by_successor(root: BSTNode | None, key: int) -> BSTNode | None:
    """删除节点，用中序后继（右子树最小值）替换"""
    if root is None:
        return None
    if key < root.val:
        root.left = delete_by_successor(root.left, key)
    elif key > root.val:
        root.right = delete_by_successor(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        succ = find_min(root.right)
        root.val = succ.val
        root.right = delete_by_successor(root.right, succ.val)
    return root


def print_tree(node: BSTNode | None, indent: int = 0, label: str = "root"):
    if node is None:
        return
    print_tree(node.right, indent + 4, "R")
    print(" " * indent + f"--{label}:{node.val}")
    print_tree(node.left, indent + 4, "L")


def inorder(node: BSTNode | None) -> list:
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def build_bst(arr: list) -> BSTNode | None:
    root = None
    for v in arr:
        root = bst_insert(root, v)
    return root


if __name__ == "__main__":
    seq = [50, 30, 70, 20, 40, 60, 80]

    # ===== 1. 构建 BST =====
    root = build_bst(seq)
    print("插入序列:", seq)
    print(f"中序遍历: {inorder(root)}")
    print("\nBST 结构:\n")
    print_tree(root)
    print("\n" + "=" * 50)

    # ===== 2. 中序前驱删除 50 =====
    t_pred = build_bst(seq)
    t_pred = delete_by_predecessor(t_pred, 50)
    print("\n删除 50（中序前驱: 左子树最大值 = 40）:")
    print(f"中序遍历: {inorder(t_pred)}\n")
    print_tree(t_pred)
    print("\n" + "=" * 50)

    # ===== 3. 中序后继删除 50 =====
    t_succ = build_bst(seq)
    t_succ = delete_by_successor(t_succ, 50)
    print("\n删除 50（中序后继: 右子树最小值 = 60）:")
    print(f"中序遍历: {inorder(t_succ)}\n")
    print_tree(t_succ)
