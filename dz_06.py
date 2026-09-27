import heapq
import random
from timeit import timeit
import matplotlib.pyplot as plt


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[0]


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]

    def size(self):
        return len(self.heap)


def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


print("Задание 1. Очередь")
queue = Queue()
queue.enqueue("первая")
queue.enqueue("вторая")
print("peek:", queue.peek())
print("dequeue:", queue.dequeue())
print("is_empty:", queue.is_empty())

print("\nЗадание 2. Обработка задач по приоритету")
print("Меньше число приоритета - раньше берем в работу")

tasks = PriorityQueue()
# добавляем не по важности, а как пришли
tasks.enqueue(("Копирование", 4), 3)
tasks.enqueue(("Срочный отчет", 2), 1)
tasks.enqueue(("Презентация", 5), 4)
tasks.enqueue(("Сканирование", 1), 2)

print("Порядок добавления: Копирование(3), Срочный отчет(1), Презентация(4), Сканирование(2)")

current_time = 0
while not tasks.is_empty():
    name, duration = tasks.dequeue()
    current_time += duration
    print(f"'{name}' ({duration} мин) завершена в момент {current_time}")

print("Вывод: вышли не в порядке добавления, а по приоритету: отчет, сканирование, копирование, презентация.")

print("\nЗадание 3. MergeSort")
unsorted = [38, 27, 43, 3, 9, 82, 10]
print(f"Было:  {unsorted}")
print(f"Стало: {merge_sort(unsorted)}")

print("\nЗадание 4. Сравнение MergeSort и пузырьком")

random.seed(42)
sizes = [10, 100, 1000]
merge_times = []
bubble_times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    merge_time = timeit(lambda a=arr: merge_sort(a), number=5)
    bubble_time = timeit(lambda a=arr: bubble_sort(a), number=5)

    merge_times.append(merge_time)
    bubble_times.append(bubble_time)

    print(f"Размер {size}:")
    print(f"  MergeSort:  {merge_time:.6f} сек")
    print(f"  Пузырьком:  {bubble_time:.6f} сек")

plt.figure(figsize=(8, 5))
plt.plot(sizes, merge_times, marker="o", label="MergeSort")
plt.plot(sizes, bubble_times, marker="o", label="Пузырьком")
plt.xlabel("Размер списка")
plt.ylabel("Время (сек)")
plt.title("MergeSort vs пузырьковая сортировка")
plt.legend()
plt.grid(True)
plt.savefig("graph_merge.png")
print("Вывод: MergeSort быстрее на больших списках. Пузырьком - O(n^2), слиянием - O(n log n).")
