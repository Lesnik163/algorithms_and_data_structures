import random
from timeit import timeit
import matplotlib.pyplot as plt


def bubble_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(arr):
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


test = [64, 25, 12, 22, 11]
print("Задание 1. Пузырьком:", bubble_sort(test))
print("Задание 2. Выбором:", selection_sort(test))
print("Дополнительно. Вставками:", insertion_sort(test))


print("\nЗадание 3. Сравнение времени")

random.seed(42) # чтобы генератор случайных чисел был один и тот же и массивы были одинаковые
sizes = [100, 200, 300, 400, 500]
bubble_times = []
selection_times = []
insertion_times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    bubble_time = timeit(lambda a=arr: bubble_sort(a), number=5)
    selection_time = timeit(lambda a=arr: selection_sort(a), number=5)
    insertion_time = timeit(lambda a=arr: insertion_sort(a), number=5)

    bubble_times.append(bubble_time)
    selection_times.append(selection_time)
    insertion_times.append(insertion_time)

    print(f"Размер {size}:")
    print(f"  пузырьком: {bubble_time:.6f} сек")
    print(f"  выбором:   {selection_time:.6f} сек")
    print(f"  вставками: {insertion_time:.6f} сек")

plt.figure(figsize=(8, 5))
plt.plot(sizes, bubble_times, marker="o", label="Пузырьком")
plt.plot(sizes, selection_times, marker="o", label="Выбором")
plt.plot(sizes, insertion_times, marker="o", label="Вставками")
plt.xlabel("Размер списка")
plt.ylabel("Время (сек)")
plt.title("Сравнение алгоритмов сортировки")
plt.legend()
plt.grid(True)
plt.savefig("graph_sort.png")

# Задание 1. Пузырьком: [11, 12, 22, 25, 64]
# Задание 2. Выбором: [11, 12, 22, 25, 64]
# Дополнительно. Вставками: [11, 12, 22, 25, 64]

# Задание 3. Сравнение времени
# Размер 100:
#   пузырьком: 0.001216 сек
#   выбором:   0.000630 сек
#   вставками: 0.000539 сек
# Размер 200:
#   пузырьком: 0.004698 сек
#   выбором:   0.002391 сек
#   вставками: 0.002455 сек
# Размер 300:
#   пузырьком: 0.012039 сек
#   выбором:   0.005967 сек
#   вставками: 0.005543 сек
# Размер 400:
#   пузырьком: 0.021798 сек
#   выбором:   0.010387 сек
#   вставками: 0.011056 сек
# Размер 500:
#   пузырьком: 0.032917 сек
#   выбором:   0.015659 сек
#   вставками: 0.016142 сек


# Вывод: все три алгоритма имеют сложность O(n^2), поэтому время растет быстро.
# На графике видно, что при увеличении размера списка время заметно увеличивается.
