# main_program.py
import random
import time
from WindowOutput import start_console


# Функции сортировки
def tournament_sort(arr):
    def find_winner(sub_arr):
        while len(sub_arr) > 1:
            winners = []
            for i in range(0, len(sub_arr), 2):
                if i + 1 < len(sub_arr):
                    winners.append(min(sub_arr[i], sub_arr[i + 1]))
                else:
                    winners.append(sub_arr[i])
            sub_arr = winners
        return sub_arr[0] if sub_arr else None

    sorted_array = []
    while arr:
        winner = find_winner(arr)
        sorted_array.append(winner)
        arr.remove(winner)
    return sorted_array


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Генерация массива
arr = [random.randint(0, 1000000) for _ in range(10000)]


# Логика программы, которая будет выполняться после запуска графического интерфейса
def run_program():
    print("Начинаем тестирование сортировок...")
    
    # Турнирная сортировка
    start_time = time.time()
    tournament_sort(arr.copy())
    print(f"Турнирная сортировка завершена за {time.time() - start_time:.6f} секунд.")
    
    # Быстрая сортировка
    start_time = time.time()
    quicksort(arr.copy())
    print(f"Быстрая сортировка завершена за {time.time() - start_time:.6f} секунд.")
    
    # Стандартная сортировка
    start_time = time.time()
    sorted(arr)
    print(f"Стандартная сортировка завершена за {time.time() - start_time:.6f} секунд.")


if __name__ == "__main__":
    # Запуск графического интерфейса
    root, app = start_console()

    # Запуск программы через 1 секунду после инициализации интерфейса
    root.after(1000, run_program)

    # Запуск главного цикла Tkinter
    root.mainloop()