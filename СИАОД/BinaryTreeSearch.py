import time
import random
import bisect

# --- Бинарное дерево поиска ---
class TreeNode:
    """Класс для представления узла бинарного дерева."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Класс для реализации бинарного дерева поиска."""
    def __init__(self):
        self.root = None

    def insert(self, value):  # Добавление значения
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):  # Рекурсивная вставка
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):  # Поиск значения
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):  # Рекурсивный поиск
        if node is None:
            return False
        if node.value == value:
            return True
        return self._search_recursive(node.left, value) if value < node.value else self._search_recursive(node.right, value)

    def delete(self, value):  # Удаление значения
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):  # Рекурсивное удаление
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None and node.right is None:  # Узел без потомков
                return None
            if node.left is None:  # Узел с одним потомком
                return node.right
            if node.right is None:
                return node.left
            min_node = self._find_min(node.right)  # Узел с двумя потомками
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        return node

    def _find_min(self, node):  # Поиск минимального узла
        while node.left is not None:
            node = node.left
        return node


# --- Хеш-таблица с простым рехэшированием ---
class HashTable:
    """Хеш-таблица с линейным пробированием."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.collisions = 0

    def hash(self, key):
        a = 3571  # Простое число для лучшего распределения
        b = 6181
        return (a * key + b) % self.capacity

    def add(self, key):
        idx = self.hash(key)
        original_idx = idx
        step = 1
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return False  # Ключ уже существует
            self.collisions += 1
            idx = (idx + step) % self.capacity
            if idx == original_idx:
                print("Таблица заполнена!")
                return False
        self.table[idx] = key
        return True

    def lookup(self, key):
        idx = self.hash(key)
        original_idx = idx
        step = 1
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return idx
            idx = (idx + step) % self.capacity
            if idx == original_idx:
                break
        return -1

    def remove(self, key):
        idx = self.hash(key)
        original_idx = idx
        step = 1
        while self.table[idx] is not None:
            if self.table[idx] == key:
                self.table[idx] = None
                return True
            idx = (idx + step) % self.capacity
            if idx == original_idx:
                break
        return False


# --- Функция измерения времени ---
def measure_time(func, *args, iterations=1000):
    total_time = 0.0
    for _ in range(iterations):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        total_time += (end - start)
    return result, total_time / iterations


# --- Основная программа ---
if __name__ == "__main__":
    # --- Настройки тестирования ---
    dataset_size = 10_000_000
    data = [random.randint(0, 10_000_000) for _ in range(dataset_size)]

    # --- Тестирование: Бинарное дерево ---
    bst = BinarySearchTree()

    # Вставка
    insert_result, insert_time = measure_time(
        lambda: [bst.insert(x) for x in data], iterations=1
    )
    print(f"Вставка в дерево заняла {insert_time:.9f} сек.")

    # Поиск
    target = random.choice(data)
    search_result, search_time = measure_time(bst.search, target)
    print(f"Поиск в дереве: {'Найден' if search_result else 'Не найден'}, время: {search_time:.9f} сек.")

    # Удаление
    delete_value = random.choice(data)
    delete_result, delete_time = measure_time(bst.delete, delete_value)
    print(f"Удаление из дерева: {'Удалён' if delete_result else 'Не найден'}, время: {delete_time:.9f} сек.")


    # --- Тестирование: Хеш-таблица ---
    table_capacity = 30011  # Увеличено для снижения коллизий
    hashtable = HashTable(table_capacity)

    # Добавляем уникальные элементы
    elements = list(set(random.randint(0, 1_000_000) for _ in range(7000)))

    # Заполнение таблицы
    for elem in elements:
        hashtable.add(elem)

    # Поиск
    search_key = random.choice(elements)
    hash_result, hash_time = measure_time(hashtable.lookup, search_key)
    print(f"Поиск в таблице: {'Найден' if hash_result != -1 else 'Не найден'}, время: {hash_time:.9f} сек.")

    # Добавление
    new_key = random.randint(0, 1_000_000)
    _, hash_insert_time = measure_time(hashtable.add, new_key)
    print(f"Добавление в таблицу заняло {hash_insert_time:.9f} сек.")

    # Удаление
    delete_key = random.choice(elements)
    _, hash_remove_time = measure_time(hashtable.remove, delete_key)
    print(f"Удаление из таблицы заняло {hash_remove_time:.9f} сек.")
    
    # --- Сравнение со встроенными структурами ---
print("\n=== Сравнение со встроенными структурами ===")

# 1. Линейный поиск в списке (in)
_, list_in_time = measure_time(lambda: target in data)
print(f"Время линейного поиска (in list): {list_in_time:.9f} сек.")

# 2. Бинарный поиск через bisect
sorted_data = sorted(data)  # Для бинарного поиска нужен отсортированный список

def bisect_search():
    idx = bisect.bisect_left(sorted_data, target)
    return idx < len(sorted_data) and sorted_data[idx] == target

_, bisect_time = measure_time(bisect_search)
print(f"Время бинарного поиска (bisect): {bisect_time:.9f} сек.")

# 3. Поиск во встроенном set
built_in_set = set(data)

_, set_lookup_time = measure_time(lambda: target in built_in_set)
print(f"Время поиска во встроенном set: {set_lookup_time:.9f} сек.")

print(f"Количество коллизий: {hashtable.collisions}")