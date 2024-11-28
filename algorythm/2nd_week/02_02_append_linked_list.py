# node 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(5)
print(node.data, node.next)

# self.next 에 다음 노드의 정보를 저장
next_node = Node(3)
node.next = next_node

# linkdelist 구현
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

# linkedList에 node를 추가하려면 맨 뒤의 노드에 추가하면된다.
# 노드추가는 어떻게 하나요? (Line:10 참고)
# 맨뒤의 노드의 특징은? 다음 node 에 대한 정보가 없다(self.next = None)!!

# append 구현(LinkedList 에 node 추가)
    # value = 연결할 새로운 노드
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    # linked_list 의 head 를 따라가면서 현재 있는 node들을 전부 출력해주는 함수.
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next




linked_list = LinkedList(5)
print(linked_list.head.data)

linked_list.append(12)

linked_list.append(8)

linked_list.print_all()