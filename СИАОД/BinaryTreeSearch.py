import random
import time
from WindowOutput import start_console


class TreeNode:                                                                 # Класс для узла бинарного дерева
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:                                                               # Класс для бинарного дерева
    def __init__(self):
        self.root = None

    def insert(self, value):                                                    # Добавление элемента в бинарное дерево
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
            else:                                                               # Если значение уже существует в дереве, выходим из цикла
                return

    def search(self, value):                                                    # Поиск элемента в бинарном дереве
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self):                                                # Итеративный обход дерева в порядке возрастания
        stack = []
        result = []
        current = self.root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result



def generate_random_data(size, min_value=0, max_value=1000000):                 # Генерация начального набора данных
    return list(set(random.randint(min_value, max_value) for _ in range(size))) # Генерация случайного массива данных


# Логика программы, которая будет выполняться после запуска графического интерфейса
def run_program(app, binary_tree, generated_data):
    def on_user_input(user_input):
        try:
            if user_input == "1":                                               # Добавление числа
                print("Введите число для добавления:")
                app.awaiting_additional_input = True
                app.additional_input_callback = lambda value: handle_add(value)

            elif user_input == "2":                                             # Поиск числа
                print("Введите число для поиска:")
                app.awaiting_additional_input = True
                app.additional_input_callback = lambda value: handle_search(value)

            elif user_input == "3":                                             # Удаление числа
                print("Введите число для удаления:")
                app.awaiting_additional_input = True
                app.additional_input_callback = lambda value: handle_delete(value)

            elif user_input == "4":                                             # Вывод дерева (обход в порядке возрастания)
                sorted_values = binary_tree.inorder_traversal()
                print("Элементы дерева в порядке возрастания:", sorted_values[:10], "...")  # Вывод первых 10 элементов

            elif user_input == "5":                                             # Сравнение времени поиска
                print("Введите число для сравнения времени поиска:")
                app.awaiting_additional_input = True
                app.additional_input_callback = lambda value: compare_search_time(value)

            elif user_input == "6":                                             # Выход из программы
                print("Программа завершена.")
                app.root.quit()

            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2, 3, 4, 5 или 6.")
        except ValueError:
            print("Ошибка: введите целое число.")

    def handle_add(value):                                                      # Функция добавления числа
        try:
            new_value = int(value)
            binary_tree.insert(new_value)
            print(f"Число {new_value} успешно добавлено.")
        except ValueError:
            print("Ошибка: введите целое число.")

    def handle_search(value):                                                   # Функция поиска числа
        try:
            search_value = int(value)
            found = binary_tree.search(search_value)
            if found:
                print(f"Число {search_value} найдено в дереве.")
            else:
                print(f"Число {search_value} не найдено в дереве.")
        except ValueError:
            print("Ошибка: введите целое число.")

    def handle_delete(value):                                                   # Функция удаления числа
        try:
            delete_value = int(value)
            binary_tree.delete(delete_value)
        except ValueError:
            print("Ошибка: введите целое число.")

    def compare_search_time(target_value_str):                                  # Функция сравнения времени работы поиска в бинарном дереве и списке
        try:
            target_value = int(target_value_str)
        except ValueError:
            print("Ошибка: введите целое число.")
            return

        # Поиск в бинарном дереве
        start_time = time.time()
        tree_found = binary_tree.search(target_value)
        tree_time = time.time() - start_time

        # Поиск в списке
        start_time = time.time()
        list_found = target_value in generated_data
        list_time = time.time() - start_time

        # Вывод результатов
        if tree_found:
            print(f"Число {target_value} найдено в бинарном дереве за {tree_time:.6f} секунд.")
        else:
            print(f"Число {target_value} не найдено в бинарном дереве за {tree_time:.6f} секунд.")

        if list_found:
            print(f"Число {target_value} найдено в списке за {list_time:.6f} секунд.")
        else:
            print(f"Число {target_value} не найдено в списке за {list_time:.6f} секунд.")

        print(f"Разница во времени: {abs(tree_time - list_time):.6f} секунд.")

    app.on_user_input = on_user_input                                           # Привязываем функцию обработки ввода к графическому интерфейсу

    print("Инициализация бинарного дерева...")

    # Генерация данных
    data_size = 100000                                                          # Размер массива
    random_data = generate_random_data(data_size)
    for i, value in enumerate(random_data):
        if i % 10000 == 0:                                                      # Вывод прогресса каждые 10000 элементов
            print(f"Добавлено {i} элементов...")
        binary_tree.insert(value)

    print("Бинарное дерево создано. Доступные операции:")
    print("1. Добавить число")
    print("2. Найти число")
    print("3. Удалить число")
    print("4. Вывести дерево (обход в порядке возрастания)")
    print("5. Сравнение времени поиска")
    print("6. Выйти")


if __name__ == "__main__":
    
    root, app = start_console()                                                 # Запуск графического интерфейса

    binary_tree = BinaryTree()                                                  # Создание бинарного дерева

    generated_data = generate_random_data(100000)                               # Генерация данных
    
    root.after(1000, lambda: run_program(app, binary_tree, generated_data))     # Запуск программы через 1 секунду после инициализации интерфейса

    root.mainloop()                                                             # Запуск главного цикла Tkinter