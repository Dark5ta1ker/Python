def quicksort(arr):                                     # Проверяем длину
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2                         # Выбираем средний элемент в качестве опорного
    pivot = arr[pivot_index]
    
    # Разделяем массив на три части
    left = [x for x in arr if x < pivot]                # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]             # Элементы, равные опорному
    right = [x for x in arr if x > pivot]               # Элементы больше опорного

    return quicksort(left) + middle + quicksort(right)  # Рекурсия...

# Тестим...
arr = [5, 3, 8, 1, 2]
print("Быстрая сортировка:", quicksort(arr))