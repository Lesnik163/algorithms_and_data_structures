
def string_hash(text):
    result = 0
    for ch in text:
        result += ord(ch)
    return result
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    def _index(self, key):
        if isinstance(key, str):
            h = string_hash(key)
        else:
            h = key
        return h % self.size

    def insert(self, key, value):
        if self.count >= self.size:
            self.resize()

        index = self._index(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def search(self, key):
        index = self._index(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._index(key)
        bucket = self.table[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self.count -= 1
                return

    def resize(self):
        items = []
        for bucket in self.table:
            items.extend(bucket)

        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for key, value in items:
            index = self._index(key)
            self.table[index].append((key, value))
            self.count += 1

def add_to_dict(table, key):
    table.insert(key, string_hash(key))


def find_in_dict(table, key):
    return table.search(key)


print("Задание 1-2. Хеш-таблица, начальный размер 5")
ht = HashTable(5)

for n in range(10):
    ht.insert(n, n * 10)
    print(f"вставили {n}, элементов {ht.count}, размер {ht.size}")

print("поиск 4:", ht.search(4))
print("поиск 100:", ht.search(100))
ht.delete(4)
print("после удаления 4:", ht.search(4))

print("\nЗадание 3. Хеш строки (сумма ASCII)")
for word in ["кот", "дом", "алгоритм"]:
    print(f"{word} -> {string_hash(word)}")

print("\nЗадание 4. Словарь: ключ - строка, значение - хеш")
words = HashTable(5)
for word in ["алгоритм", "поиск", "хеш", "таблица"]:
    add_to_dict(words, word)

print("хеш 'поиск':", find_in_dict(words, "поиск"))
print("хеш 'нет':", find_in_dict(words, "нет"))

result = {}
for bucket in words.table:
    for key, value in bucket:
        result[key] = value
print("словарь:", result)