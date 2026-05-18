class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.set = [ListNode(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        cur = self.set[key%(10**4)]
        while cur.next != None:
            cur = cur.next
            if cur.key == key:
                cur.value = value
                return
        cur.next = ListNode(key, value)
        return

    def get(self, key: int) -> int:
        cur = self.set[key%(10**4)]
        while cur.next != None:
            cur = cur.next
            if cur.key == key:
                return cur.value
        return -1

    def remove(self, key: int) -> None:
        cur = self.set[key%(10**4)]
        while cur.next != None:
            if cur.next.key == key:
                cur.next = cur.next.next
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)