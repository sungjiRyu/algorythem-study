class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # def get_kth_node_from_last(self, k):
    #     length = 1
    #     cur = self.head
    #
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #
    #     end_length = length - k
    #
    #     cur = self.head
    #
    #     for i in range(end_length):
    #         cur = cur.next
    #
    #     return cur

    # 두개의 포인터(fast, slow)를 이용한 방법
    def get_kth_node_from_last(self, k):
        fast = self.head
        slow = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
