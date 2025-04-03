# WindowOutput.py
import sys
import tkinter as tk
from io import StringIO


class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        """Перенаправление вывода в текстовое поле."""
        self.text_widget.config(state=tk.NORMAL)  # Разблокируем текстовое поле
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)  # Автопрокрутка до последней строки
        self.text_widget.config(state=tk.DISABLED)  # Блокируем текстовое поле

    def flush(self):
        """Обязательный метод для совместимости с sys.stdout."""
        pass


class ConsoleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графическая консоль")

        # Текстовое поле для вывода
        self.output_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Поле для ввода команд
        self.input_entry = tk.Entry(root)
        self.input_entry.pack(fill=tk.X, padx=5, pady=5)
        self.input_entry.bind("<Return>", self.process_input)  # Обработка нажатия Enter

        # Перенаправление stdout и stderr
        sys.stdout = ConsoleRedirector(self.output_text)
        sys.stderr = ConsoleRedirector(self.output_text)

        # Приветственное сообщение
        print("Добро пожаловать в графическую консоль!")
        print("Введите команду ниже и нажмите Enter.")

        # Состояние для дополнительного ввода
        self.awaiting_additional_input = False
        self.additional_input_callback = None

    def process_input(self, event=None):
        """Обработка ввода пользователя."""
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)  # Очистка поля ввода

        if self.awaiting_additional_input and self.additional_input_callback:
            # Если ожидается дополнительный ввод, передаем его в callback
            self.additional_input_callback(user_input)
            self.awaiting_additional_input = False
            self.additional_input_callback = None
        else:
            # Вывод введенной команды в текстовое поле
            print(f">>> {user_input}")

            # Передача ввода в основную программу
            if hasattr(self, "on_user_input"):
                self.on_user_input(user_input)


def start_console():
    """
    Запуск графического интерфейса.
    Эта функция может быть импортирована и использована в других программах.
    """
    root = tk.Tk()
    app = ConsoleApp(root)
    return root, app