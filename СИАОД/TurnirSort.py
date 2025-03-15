import time
import random

def tournament_sort(arr):                                                   # Строим турнирное дерево...    
    def find_winner(sub_arr):
        while len(sub_arr) > 1:
            winners = []
            for i in range(0, len(sub_arr), 2):
                if i + 1 < len(sub_arr):                                    # Выбираем кого повесить... на доску почета.                                        
                    winners.append(min(sub_arr[i], sub_arr[i + 1]))
                else:                                                       # Если остался непарный элемент, он дерется со своей тенью
                    winners.append(sub_arr[i])
            sub_arr = winners
        return sub_arr[0] if sub_arr else None

    sorted_array = []
    while arr:
        winner = find_winner(arr)                                           # Находим победителя (минимальный элемент)
        sorted_array.append(winner)                                         # Добавляем победителя в отсортированный массив
        arr.remove(winner)                                                  # Удаляем победителя из исходного массива
    return sorted_array

def quicksort(arr):                                                         # Проверяем длину
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2                         # Выбираем средний элемент в качестве опорного
    pivot = arr[pivot_index]
    
    # Разделяем массив на три части
    left = [x for x in arr if x < pivot]                # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]             # Элементы, равные опорному
    right = [x for x in arr if x > pivot]               # Элементы больше опорного

    return quicksort(left) + middle + quicksort(right)  # Рекурсия...

# Генерация массива
arr = [random.randint(0, 1000000) for _ in range(100000)]

# Турнирная сортировка
start_time = time.time()
tournament_sort(arr.copy())
print("Турнирная сортировка: {:.6f} секунд".format(time.time() - start_time))

# Быстрая сортировка
start_time = time.time()
quicksort(arr.copy())
print("Быстрая сортировка: {:.6f} секунд".format(time.time() - start_time))

# Стандартная сортировка Python
start_time = time.time()
sorted(arr)
print("Стандартная сортировка: {:.6f} секунд".format(time.time() - start_time))





