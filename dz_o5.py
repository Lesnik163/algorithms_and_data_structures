import random
from timeit import timeit
import matplotlib.pyplot as plt

def fibonacci(n, depth=0):
    print("  " * depth + f"-> fib({n})")
    if n <= 0:
        print("  " * depth + f"<- fib({n}) = 0")
        return 0
    if n == 1:
        print("  " * depth + f"<- fib({n}) = 1")
        return 1
    result = fibonacci(n - 1, depth + 1) + fibonacci(n - 2, depth + 1)
    print("  " * depth + f"<- fib({n}) = {result}")
    return result


def find_max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return left_max if left_max > right_max else right_max


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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    merge_sort(left_half)
    merge_sort(right_half)
    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print("Задание 1. Фибоначчи n=5, стек вызовов:")
print("-> вход в функцию, <- выход (LIFO)")
result = fibonacci(5)
print(f"Ответ: fib(5) = {result}")
print("Вывод: глубина стека до 5 уровней, много повторных вызовов (fib(3), fib(2)...)")

print("\nЗадание 4. Сравнение QuickSort и сортировки вставками")

random.seed(42)
sizes = [10, 100, 1000]
quick_times = []
insertion_times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    quick_time = timeit(lambda a=arr: quicksort(a), number=5)
    insertion_time = timeit(lambda a=arr: insertion_sort(a), number=5)

    quick_times.append(quick_time)
    insertion_times.append(insertion_time)

    print(f"Размер {size}:")
    print(f"  QuickSort:  {quick_time:.6f} сек")
    print(f"  Вставками:  {insertion_time:.6f} сек")

plt.figure(figsize=(8, 5))
plt.plot(sizes, quick_times, marker="o", label="QuickSort")
plt.plot(sizes, insertion_times, marker="o", label="Вставками")
plt.xlabel("Размер списка")
plt.ylabel("Время (сек)")
plt.title("QuickSort vs сортировка вставками")
plt.legend()
plt.grid(True)
plt.savefig("graph_quicksort.png")
