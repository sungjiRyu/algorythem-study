dict = {"fast": "빠른"}

# put(key, value) -> dict 에 key 에 해당하는 곳에 value 를 저장
# get(key) -> dictionary 에 key 에 해당하는 value 를 반환

class Dict:
    def __init__(self):
        self.items = [None] * 8


    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("fast", "빠른")
print(my_dict.get("fast"))
