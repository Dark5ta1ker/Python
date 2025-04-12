import time
import sys
import tkinter as tk
from tkinter import messagebox
import turtle



def draw_triangle(t, points, color):                                                    # Функция для рисования треугольника
    t.fillcolor(color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()

def sierpinski(t, points, depth):                                                       # Рекурсивная функция для генерации фрактала Салфетки Серпинского
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(t, points, colormap[depth % len(colormap)])

    if depth > 0:                                                                       # Вычисляем середины сторон треугольника
        mid1 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
        mid2 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
        mid3 = ((points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2)

        # Рекурсивно вызываем функцию для трех новых треугольников
        sierpinski(t, [points[0], mid1, mid3], depth - 1)
        sierpinski(t, [mid1, points[1], mid2], depth - 1)
        sierpinski(t, [mid3, mid2, points[2]], depth - 1)

def run_program():                                                                      # Логика программы
    def on_generate():
        try:
            depth = int(depth_entry.get())
            if depth < 0:
                raise ValueError("Глубина должна быть неотрицательным числом.")
            generate_fractal(depth)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def generate_fractal(depth):                                                        # Генерирует фрактал и измеряет время выполнения
        start_time = time.time()

        # Инициализация черепахи
        screen = turtle.Screen()
        screen.title("Фрактал Салфетки Серпинского")
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()

        points = [[-200, -100], [0, 200], [200, -100]]                                  # Начальные точки большого треугольника

        sierpinski(t, points, depth)                                                    # Рисуем фрактал

        # Завершение
        end_time = time.time()
        execution_time = end_time - start_time
        screen.onclick(lambda x, y: screen.bye())  # Закрытие окна по клику
        print(f"Глубина: {depth}, Время выполнения: {execution_time:.6f} секунд.")

    def show_recursion_limit():                                                         # Показывает максимальную глубину рекурсии
        recursion_limit = sys.getrecursionlimit()
        messagebox.showinfo("Максимальная глубина рекурсии", f"Максимальная глубина рекурсии: {recursion_limit}")

    # Создание графического интерфейса
    root = tk.Tk()
    root.title("Генератор фрактала Салфетки Серпинского")

    tk.Label(root, text="Введите глубину фрактала:").pack(pady=5)
    depth_entry = tk.Entry(root)
    depth_entry.pack(pady=5)

    tk.Button(root, text="Сгенерировать фрактал", command=on_generate).pack(pady=5)
    tk.Button(root, text="Показать глубину рекурсии", command=show_recursion_limit).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    run_program()