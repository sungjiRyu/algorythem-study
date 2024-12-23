class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 현재  = [4]
# [3] 추가
#[4] -> [3]
class Stack:
    def __init__(self):
        self.head = None

# 3을 추가
    def push(self, value):
        new_head = Node(value) # value( = 3) 을 현재 헤드에 추가
        new_head.next = self.head # 현재노드(3) 가 이전노드(4) 를 바라보게
        self.head = new_head # 현재 헤드(최상단)를 추가(pop) 한 노드로 설정

        return

    # pop 기능 구현
    # 현재 헤드를 반환하고 다음 노드를 헤드로 설정
    def pop(self):
        if self.is_empty():
            return print("stack is Empty")

        delete_head = self.head
        self.head = delete_head.next

        return delete_head

    # 최상단의 값을 조회
    def peek(self):
        if self.is_empty():
            return "stack is Empty"
        return self.head.data

    # isEmpty 기능 구현(현재스택에 값이 존재한는지 여부 반환)
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())
stack.pop()

