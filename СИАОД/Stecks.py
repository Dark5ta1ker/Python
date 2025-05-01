class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):                                             # Проверяет, пуст ли стек
        return len(self.items) == 0

    def push(self, item):                                           # Добавляет элемент в начало стека
        self.items.append(item)

    def pop(self):                                                  # Извлекает элемент из начала стека
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):                                                 # Возвращает последний элемент стека без удаления
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")


def process_file(file_path):                                        # Обрабатывает файл и выводит символы в требуемом порядке
    
    letters_stack = Stack()                                         # Инициализация стеков
    digits_stack = Stack()
    others_stack = Stack()

    
    with open(file_path, 'r') as file:                              # Чтение файла и заполнение стеков
        for char in file.read():
            if char.isalpha():                                      # Если символ — буква
                letters_stack.push(char)
            elif char.isdigit():                                    # Если символ — цифра
                digits_stack.push(char)
            else:                                                   # Все остальные символы
                others_stack.push(char)


    def extract_stack(stack):                                       # Извлечение данных из стеков в правильном порядке

        temp = []
        while not stack.is_empty():
            temp.append(stack.pop())
        return ''.join(reversed(temp))

    
    letters = extract_stack(letters_stack)                          # Формирование результата
    digits = extract_stack(digits_stack)
    others = extract_stack(others_stack)

    
    print(letters + digits + others)                                # Вывод результата


file_path = "E:/Мои документы/Desktop/Уроки/Python/СИАОД/text.txt"  # Укажите путь к вашему файлу
process_file(file_path)