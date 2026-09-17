from timeit import timeit
import matplotlib.pyplot as plt
from constants import (
    SORTED_NUMBERS,
    BINARY_FIRST,
    BINARY_MIDDLE,
    BINARY_LAST,
    BINARY_MISSING,
)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- Задание 2. Сложность бинарного поиска ---
#
# Время: O(log n). На каждом шаге отбрасываем половину списка.
# В лучшем случае элемент посередине - O(1).
# В худшем - O(log n).
#
# Память: O(1). Используем только low, high и mid.


print("Задание 3. Отсортированный список из 100 чисел")

for value in [BINARY_FIRST, BINARY_MIDDLE, BINARY_LAST, BINARY_MISSING]:
    result = binary_search(SORTED_NUMBERS, value)
    elapsed = timeit(lambda v=value: binary_search(SORTED_NUMBERS, v), number=1000)
    print(f"Ищем {value}, индекс: {result}, время: {elapsed:.6f} сек (1000 запусков)")
# Задание 3. Отсортированный список из 100 чисел
# Ищем 3, индекс: 0, время: 0.000376 сек (1000 запусков)
# Ищем 214, индекс: 50, время: 0.000378 сек (1000 запусков)
# Ищем 498, индекс: 99, время: 0.000456 сек (1000 запусков)
# Ищем 9999, индекс: -1, время: 0.000481 сек (1000 запусков)

print("\nЗадание 4. Сравнение линейного и бинарного поиска")

sizes = [100, 1000, 10000, 100000]
linear_times = []
binary_times = []

for size in sizes:
    arr = list(range(size))
    target = size - 1  # последний элемент для максимальной сложности

    linear_time = timeit(lambda: linear_search(arr, target), number=100)
    binary_time = timeit(lambda: binary_search(arr, target), number=1000)

    linear_times.append(linear_time)
    binary_times.append(binary_time)

    print(f"Размер {size}:")
    print(f"линейный: {linear_time:.6f} сек")
    print(f"бинарный: {binary_time:.6f} сек")

plt.figure(figsize=(8, 5))
plt.plot(sizes, linear_times, marker="o", color="blue")
plt.xlabel("Размер списка")
plt.ylabel("Время (сек)")
plt.title("Линейный поиск O(n)")
plt.grid(True)
plt.savefig("graph_linear.png")

plt.figure(figsize=(8, 5))
plt.plot(sizes, binary_times, marker="o", color="green")
plt.xlabel("Размер списка")
plt.ylabel("Время (сек)")
plt.title("Бинарный поиск O(log n)")
plt.grid(True)
plt.savefig("graph_binary.png")

# Задание 4. Сравнение линейного и бинарного поиска
# Размер 100:
# линейный: 0.000164 сек
# бинарный: 0.000431 сек
# Размер 1000:
# линейный: 0.001986 сек
# бинарный: 0.000806 сек
# Размер 10000:
# линейный: 0.021763 сек
# бинарный: 0.001214 сек
# Размер 100000:
# линейный: 0.219885 сек
# бинарный: 0.001405 сек

# Вывод: линейный поиск растет примерно пропорционально размеру списка O(n).
# Бинарный почти не меняется при росте списка - это O(log n).
