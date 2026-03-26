class MultipleDict:
    def __init__(self, size: int):
        self.size: int = size
        self.table: list[list[tuple[str, int]]] = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        """使用Python内置哈希函数"""
        # Python的hash()返回一个整数，可能为负数，取绝对值后取模
        return abs(hash(key)) % self.size

    def put(self, key: str, value: int) -> None:
        """插入或更新键值对"""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        # 检查键是否已存在
        for i, (old_key, old_value) in enumerate(bucket):
            if key == old_key:
                bucket[i] = (key, value)  # 更新
                return

        # 键不存在，添加新键值对
        bucket.append((key, value))

    def get(self, key: str) -> int:
        """获取键对应的值，如果键不存在则抛出KeyError"""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for old_key, old_value in bucket:
            if key == old_key:
                return old_value

        raise KeyError(f"Key '{key}' not found")

    def get_default(self, key: str, default=None):
        """获取键对应的值，如果键不存在则返回默认值"""
        try:
            return self.get(key)
        except KeyError:
            return default

    def remove(self, key: str) -> int:
        """删除键值对并返回被删除的值"""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for i, (old_key, old_value) in enumerate(bucket):
            if key == old_key:
                del bucket[i]
                return old_value

        raise KeyError(f"Key '{key}' not found")

    def contains(self, key: str) -> bool:
        """检查键是否存在"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self) -> int:
        """返回哈希表中键值对的数量"""
        return sum(len(bucket) for bucket in self.table)

    def __str__(self) -> str:
        """返回哈希表的字符串表示"""
        items = []
        for i, bucket in enumerate(self.table):
            if bucket:
                items.append(f"Bucket {i}: {bucket}")
        return "{\n  " + "\n  ".join(items) + "\n}"