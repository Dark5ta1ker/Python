import time
from WindowOutput import start_console


# Алгоритм Кнута-Морриса-Пратта (КМП)
def compute_lps_array(pattern):
    lps = [0] * len(pattern)                                        # Вычисление массива LPS (longest prefix suffix).
    length = 0                                                      # Длина текущего префикса
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern, case_sensitive=True):                 # Поиск подстроки в строке с использованием алгоритма КМП.

    if not case_sensitive:
        text = text.lower()
        pattern = pattern.lower()

    lps = compute_lps_array(pattern)
    i = 0                                                           # Индекс для text
    j = 0                                                           # Индекс для pattern
    positions = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


# Логика программы
def run_program(app):
    strings = []                                                    # Хранилище строк
    case_sensitive = True                                           # Флаг чувствительности к регистру

    def on_user_input(user_input):
        try:
            if user_input == "1":                                   # Добавление строки
                print("Введите строку для добавления:")
                app.awaiting_additional_input = True
                app.additional_input_callback = lambda value: handle_add_string(value)

            elif user_input == "2":                                 # Ввод подстроки
                print("Введите подстроку для поиска:")
                app.awaiting_additional_input = True
                app.additional_input_callback = lambda value: handle_search_substring(value)

            elif user_input == "3":                                 # Переключение чувствительности к регистру
                toggle_case_sensitivity()

            elif user_input == "4":                                 # Сравнение времени работы алгоритмов
                compare_search_time()

            elif user_input == "5":                                 # Выход из программы
                print("Программа завершена.")
                app.root.quit()

            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2, 3, 4 или 5.")
        except ValueError:
            print("Ошибка: введите корректные данные.")

    def handle_add_string(value):                                   # Добавление строки в хранилище
        strings.append(value)
        print(f"Строка '{value}' успешно добавлена.")

    def handle_search_substring(substring):                         # Поиск подстроки во всех добавленных строках
        if not strings:
            print("Нет добавленных строк для поиска.")
            return

        print(f"Ищем подстроку '{substring}'...")
        results = []
        for idx, string in enumerate(strings):
            positions = kmp_search(string, substring, case_sensitive)
            if positions:
                results.append((idx, positions))

        if results:
            for idx, positions in results:
                print(f"Подстрока найдена в строке {idx} на позициях: {positions}")
        else:
            print(f"Подстрока '{substring}' не найдена ни в одной из строк.")

    def toggle_case_sensitivity():                                  # Переключение чувствительности к регистру
        nonlocal case_sensitive
        case_sensitive = not case_sensitive
        mode = "чувствительный" if case_sensitive else "нечувствительный"
        print(f"Режим поиска изменен на {mode} к регистру.")

    def compare_search_time():                                      # Сравнение времени работы алгоритмов поиска
        if not strings:
            print("Нет добавленных строк для сравнения времени.")
            return

        print("Введите подстроку для сравнения времени поиска:")
        app.awaiting_additional_input = True
        app.additional_input_callback = lambda value: handle_compare_search_time(value)

    def handle_compare_search_time(substring):                      # Обработка сравнения времени работы алгоритмов
        total_kmp_time = 0
        total_find_time = 0

        for idx, string in enumerate(strings):
            # Измерение времени для алгоритма КМП
            start_time = time.time()
            kmp_positions = kmp_search(string, substring, case_sensitive)
            kmp_time = time.time() - start_time
            total_kmp_time += kmp_time

            # Измерение времени для стандартной функции str.find()
            start_time = time.time()
            find_position = string.lower().find(substring.lower()) if not case_sensitive else string.find(substring)
            find_time = time.time() - start_time
            total_find_time += find_time

        # Вывод результатов
        print(f"Среднее время поиска алгоритмом КМП: {total_kmp_time / len(strings):.6f} секунд.")
        print(f"Среднее время поиска функцией str.find(): {total_find_time / len(strings):.6f} секунд.")
        print(f"Разница во времени: {abs(total_kmp_time - total_find_time):.6f} секунд.")

    app.on_user_input = on_user_input                               # Привязываем функцию обработки ввода к графическому интерфейсу

    print("Доступные операции:")
    print("1. Добавить строку")
    print("2. Найти подстроку")
    print("3. Переключить чувствительность к регистру")
    print("4. Сравнить время работы алгоритмов поиска")
    print("5. Выйти")


if __name__ == "__main__":
    
    root, app = start_console()                                     # Запуск графического интерфейса

    root.after(1000, lambda: run_program(app))                      # Запуск программы через 1 секунду после инициализации интерфейса

    root.mainloop()                                                 # Запуск главного цикла Tkinter