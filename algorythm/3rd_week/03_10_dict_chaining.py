dict = {"fast": "빠른"}

# 1. Chaning 기법 : 해시충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리한다.
# 2. oppen addressing(개방주소법) : 해시충돌이 발생했을 때 그 다음에 비어있는 칸에 value 를 넣어준다.
class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key,value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()

linked_tuple.add("444", 4)
linked_tuple.add("555", 5)

print(linked_tuple.items)
print(linked_tuple.get("444"))


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple)

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # index 번째의 LinkedTuple [(key, vlaue)]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


my_dict = LinkedDict()
# 해시 충돌값
# hash("444") % 8 = hash("555") % 8
my_dict.put("fast", "빠른")
print(my_dict.get("fast"))
