class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨뒤에 삽입
    def enqueue(self, value):
        new_node = Node(value)
        if queue.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

        return

    # 맨앞 노드를 가져옴
    def dequeue(self):
        if self.head is None:
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    # 맨앞 노드 확인
    def peek(self):

        if self.head is None:
            return "Queue is Empty"

        return self.head.data

    # 큐가 비었는지 확인
    def is_empty(self):

        return self.head is None

queue = Queue()
queue.enqueue(1)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())
queue.dequeue()
print(queue.peek())
