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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):

        # 추가할 노드를 만든다
        new_node = Node(value)

        # index == 0 일때,
        if index == 0:
            # 현재 헤드(첫번째 노드) 를 추가할 노드의 다음으로 이어준다
            new_node.next = self.head
            # 헤드를 추가할 노드로 설정한다
            self.head = new_node

            return

        # 추가할 노드의 이전(-1) 노드를 가져옴
        prev_node = self.get_node(index - 1)
        # 이전 노드의 다음 노드 정보 저장
        next_node = prev_node.next
        # 이전 노드와 추가할 노드와 이어줌
        prev_node.next = new_node
        # 추가한 노드와 원래 이전 노드와 이어져 있던 노드(next_node)를 이어줌
        new_node.next = next_node

        print("index 위치에 value 를 가진 Node 를 추가해주세요")

    def delete_node(self, index):

        if index == 0:
            self.head = self.get_node(1)

            return

        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next

        print("index 번째 node 를 제거해주세요!")


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(1,6)
linked_list.add_node(0,7)

# linked_list.delete_node(0)
linked_list.print_all()

