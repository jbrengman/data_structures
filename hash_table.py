class HashTable:

    def __init__(self, slots=32):  # Only need 32 slots due to hash function
        self.bucket_list = []
        for x in range(slots):
            self.bucket_list.append(HashBucket())

    def set(self, key, value):
        if type(key) != str:
            raise ValueError('Key must be a string')
        hashed = self.hasher(key)
        if not self.bucket_list[hashed]:
            self.bucket_list[hashed] = HashBucket()
        self.bucket_list[hashed].add(key, value)

    def get(self, key):
        hashed = self.hasher(key)
        return self.bucket_list[hashed].get_val(key)

    def hasher(self, key):
        hashed = 0
        for c in key:
            hashed += ord(c)
        hashed = hashed % 31
        return hashed


class HashBucket:

    def __init__(self):
        self.key_list = []
        self.value_list = []
        self.depth = 0

    def add(self, key, val):
        if key in self.key_list:  # Overwrite value if key already exists
            self.value_list[self.key_list.index(key)] = val
            return
        self.key_list.append(key)
        self.value_list.append(val)
        self.depth += 1

    def get_val(self, key):
        for x in range(self.depth):
            if self.key_list[x] == key:
                return self.value_list[x]
        raise IndexError('Not found')
