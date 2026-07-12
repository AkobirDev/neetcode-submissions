class MyHashSet:

    def __init__(self):
        self.buckets = 1000
        self.array = [[] for _ in range(self.buckets)]

    def _hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        bucket = self.array[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.array[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.array[self._hash(key)]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)