class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def reverse(self):
        """原地反转链表"""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def has_cycle(self) -> bool:
        """快慢指针判断链表是否有环"""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result


if __name__ == "__main__":
    # ===== 反转测试 =====
    ll = LinkedList()
    for x in [1, 2, 3, 4, 5]:
        ll.append(x)
    print("反转前:", ll.to_list())
    ll.reverse()
    print("反转后:", ll.to_list())

    # 单节点
    ll1 = LinkedList()
    ll1.append(42)
    ll1.reverse()
    print("单节点反转:", ll1.to_list())

    # 空链表
    ll2 = LinkedList()
    ll2.reverse()
    print("空链表反转:", ll2.to_list())

    # ===== 环检测测试 =====
    no_cycle = LinkedList()
    for x in [1, 2, 3]:
        no_cycle.append(x)
    print(f"\n无环链表: {no_cycle.has_cycle()}")

    # 构造有环链表: 1 -> 2 -> 3 -> 1
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.next = n2
    n2.next = n3
    n3.next = n1
    has_cycle_ll = LinkedList()
    has_cycle_ll.head = n1
    print(f"有环链表: {has_cycle_ll.has_cycle()}")
