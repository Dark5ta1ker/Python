import time
import random

# --- Часть 1: Бинарное дерево поиска ---

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

    def insert(self, value):
        """Добавляет значение в бинарное дерево."""
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Рекурсивно добавляет значение в поддерево."""
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

    def search(self, value):
        """Ищет значение в бинарном дереве."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Рекурсивно ищет значение в поддереве."""
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        """Удаляет значение из бинарного дерева."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Рекурсивно удаляет значение из поддерева."""
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Случай 1: Узел без потомков
            if node.left is None and node.right is None:
                return None
            # Случай 2: Узел с одним потомком
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Случай 3: Узел с двумя потомками
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        return node

    def _find_min(self, node):
        """Находит минимальный узел в поддереве."""
        while node.left is not None:
            node = node.left
        return node

# --- Часть 2: Хеш-таблица с рехэшированием ---

class HashTable:
    """Хеш-таблица с простым рехэшированием для разрешения коллизий."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.collision_count = 0

    def hash(self, key):
        """Вычисляет хеш для ключа."""
        return key % self.capacity

    def add(self, key):
        """Добавляет ключ в таблицу."""
        idx = self.hash(key)
        original_idx = idx
        step = 1
        while self.table[idx] is not None:
            self.collision_count += 1
            idx = (original_idx + step) % self.capacity
            step += 1
            if idx == original_idx:
                print("Таблица полностью заполнена!")
                return False
        self.table[idx] = key
        return True

    def lookup(self, key):
        """Ищет ключ в таблице."""
        idx = self.hash(key)
        original_idx = idx
        step = 1
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return idx
            idx = (original_idx + step) % self.capacity
            step += 1
            if idx == original_idx:
                break
        return -1

    def remove(self, key):
        """Удаляет ключ из таблицы."""
        idx = self.hash(key)
        original_idx = idx
        step = 1
        while self.table[idx] is not None:
            if self.table[idx] == key:
                self.table[idx] = None
                return True
            idx = (original_idx + step) % self.capacity
            step += 1
            if idx == original_idx:
                break
        return False

# --- Измерение производительности ---

def time_function(func, *args, iterations=100):
    """Измеряет среднее время выполнения функции."""
    total_time = sum(time.time() - time.time() for _ in range(iterations))
    result = func(*args)
    return result, total_time / iterations

# --- Основная программа ---

if __name__ == "__main__":
    # --- Бинарное дерево поиска ---
    dataset_size = 1_000_000
    raw_data = [random.randint(0, 1_000_000) for _ in range(dataset_size)]
    bst = BinarySearchTree()

    # Вставка данных в бинарное дерево
    start_time_insert = time.time()
    for value in raw_data:
        bst.insert(value)
    insert_duration = time.time() - start_time_insert
    print(f"Вставка данных в бинарное дерево заняла {insert_duration:.6f} секунд.")

    # Поиск элемента в бинарном дереве
    search_target = random.choice(raw_data) if raw_data else None
    search_result, search_time = time_function(bst.search, search_target) if search_target else (False, 0)
    print(f"Поиск в бинарном дереве: {'Элемент найден' if search_result else 'Элемент не найден'} "
          f"(время: {search_time:.6f} сек).")

    # Удаление элемента из бинарного дерева
    delete_value = random.choice(raw_data) if raw_data else None
    delete_result, delete_time = time_function(bst.delete, delete_value) if delete_value else (False, 0)
    print(f"Удаление из бинарного дерева: {'Элемент удален' if delete_result else 'Элемент не найден'} "
          f"(время: {delete_time:.6f} сек).")

    # --- Хеш-таблица ---
    table_capacity = 20011  # Простое число
    hashtable = HashTable(table_capacity)

    # Заполнение таблицы
    elements_to_add = [random.randint(0, 200) for _ in range(7000)]
    for elem in elements_to_add:
        hashtable.add(elem)

    # Поиск элемента
    search_key = random.randint(0, 200)
    hash_result, hash_time = time_function(hashtable.lookup, search_key)
    print(f"Поиск в хеш-таблице: {'Элемент найден' if hash_result != -1 else 'Элемент не найден'} "
          f"(время: {hash_time:.6f} сек).")

    # Добавление элемента
    new_key = random.randint(0, 200)
    _, hash_insert_time = time_function(hashtable.add, new_key)
    print(f"Добавление в хеш-таблицу заняло {hash_insert_time:.6f} секунд.")

    # Удаление элемента
    delete_key = random.choice(elements_to_add) if elements_to_add else None
    _, hash_remove_time = time_function(hashtable.remove, delete_key) if delete_key else (None, 0)
    print(f"Удаление из хеш-таблицы заняло {hash_remove_time:.6f} секунд." if delete_key else "Нечего удалять.")

    print(f"Количество коллизий: {hashtable.collision_count}")