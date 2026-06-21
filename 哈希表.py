def djb2_hash(key: str, table_size: int) -> int:
    """DJB2 哈希函数: hash = hash * 33 + c"""
    h = 5381
    for ch in key:
        h = ((h << 5) + h) + ord(ch)
    return h % table_size


class HashTable:
    def __init__(self, initial_size: int = 8):
        self._size = initial_size
        self._count = 0
        self._buckets = [[] for _ in range(self._size)]

    def _hash(self, key: str) -> int:
        return djb2_hash(key, self._size)

    def _load_factor(self) -> float:
        return self._count / self._size

    def _resize(self):
        old_buckets = self._buckets
        self._size *= 2
        self._count = 0
        self._buckets = [[] for _ in range(self._size)]
        for bucket in old_buckets:
            for key, val in bucket:
                self.put(key, val)

    def put(self, key: str, value):
        if self._load_factor() > 0.75:
            self._resize()

        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._count += 1

    def get(self, key: str):
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key: str):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return
        raise KeyError(f"Key '{key}' not found")

    def contains(self, key: str) -> bool:
        idx = self._hash(key)
        for k, _ in self._buckets[idx]:
            if k == key:
                return True
        return False

    def __str__(self):
        lines = []
        for i, bucket in enumerate(self._buckets):
            if bucket:
                lines.append(f"  [{i}]: {bucket}")
        return "{\n" + "\n".join(lines) + "\n}"


if __name__ == "__main__":
    ht = HashTable()

    # 基本插入
    ht.put("apple", 10)
    ht.put("banana", 20)
    ht.put("cherry", 30)
    print("插入 apple/banana/cherry 后:")
    print(ht)
    print(f'get("apple"):', ht.get("apple"))
    print(f'contains("banana"):', ht.contains("banana"))
    print(f'contains("grape"):', ht.contains("grape"))

    # 更新已有 key
    ht.put("apple", 99)
    print('\n更新 apple=99 后:')
    print(ht)
    print(f'get("apple"):', ht.get("apple"))

    # 删除
    ht.remove("banana")
    print('\n删除 banana 后:')
    print(ht)

    # 触发扩容
    print("\n插入 20 个元素触发扩容:")
    for i in range(20):
        ht.put(f"key{i}", i)
    print(f"当前桶数: {ht._size}, 元素数: {ht._count}")
    print(ht)

    # 删除不存在的 key
    try:
        ht.remove("notexist")
    except KeyError as e:
        print("\n删除不存在的 key:", e)
