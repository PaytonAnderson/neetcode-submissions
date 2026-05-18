class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % (10**4)]
        while cur.next != None:
            cur = cur.next
            if cur.key == key:
                return
        cur.next = ListNode(key)
        return

    def remove(self, key: int) -> None:
        cur = self.set[key % (10**4)]
        while cur.next != None:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return 

    def contains(self, key: int) -> bool:
        cur = self.set[key % (10**4)]
        while cur.next != None:
            cur = cur.next
            if cur.key == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)