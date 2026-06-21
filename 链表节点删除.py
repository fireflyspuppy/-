class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """尾部追加节点"""
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete_by_value(self, val):
        """删除第一个值等于 val 的节点"""
        if not self.head:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        prev = self.head
        cur = self.head.next
        while cur:
            if cur.data == val:
                prev.next = cur.next
                return
            prev, cur = cur, cur.next

    def delete_by_index(self, index: int):
        """删除第 index 个节点（从 0 开始）"""
        if not self.head or index < 0:
            return

        if index == 0:
            self.head = self.head.next
            return

        prev = self.head
        cur = self.head.next
        i = 1
        while cur:
            if i == index:
                prev.next = cur.next
                return
            prev, cur = cur, cur.next
            i += 1

    def delete_tail(self):
        """删除尾部节点"""
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return

        prev = self.head
        cur = self.head.next
        while cur.next:
            prev, cur = cur, cur.next
        prev.next = None

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    for x in [10, 20, 30, 20, 40]:
        ll.append(x)
    print("初始链表:", ll.to_list())

    ll.delete_by_value(20)
    print("删除第一个 20:", ll.to_list())

    ll.delete_by_index(1)
    print("删除下标 1:", ll.to_list())

    ll.delete_tail()
    print("删除尾部:", ll.to_list())

    ll.delete_by_value(10)
    print("删除 10 (头节点):", ll.to_list())

    ll.delete_by_value(999)
    print("删除不存在的 999:", ll.to_list())
