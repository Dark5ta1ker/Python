import time
import sys
import tkinter as tk
from tkinter import messagebox
import turtle


def sierpinski_a(t, length, depth):  # Тип A
    if depth == 0:
        t.forward(length)
        return
    sierpinski_b(t, length, depth - 1)
    t.left(60)
    sierpinski_a(t, length, depth - 1)
    t.left(60)
    sierpinski_b(t, length, depth - 1)

def sierpinski_b(t, length, depth):  # Тип B
    if depth == 0:
        t.forward(length)
        return
    sierpinski_a(t, length, depth - 1)
    t.right(60)
    sierpinski_b(t, length, depth - 1)
    t.right(60)
    sierpinski_a(t, length, depth - 1)


def run_program():
    def on_generate():
        try:
            depth = int(depth_entry.get())
            if depth < 0:
                raise ValueError("Глубина должна быть неотрицательным числом.")
            generate_fractal(depth)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def generate_fractal(depth):
        start_time = time.time()

        screen = turtle.Screen()
        screen.title("Кривая Серпинского")
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        t.goto(-250, -250)
        t.pendown()

        length = 5  # Длина базового отрезка (можно увеличить для большего масштаба)

        # Рисуем кривую Серпинского
        for i in range(3):
            sierpinski_a(t, length, depth)
            t.right(120)

        end_time = time.time()
        execution_time = end_time - start_time
        screen.onclick(lambda x, y: screen.bye())  # Закрытие по клику
        print(f"Глубина: {depth}, Время выполнения: {execution_time:.6f} секунд.")

    def show_recursion_limit():
        recursion_limit = sys.getrecursionlimit()
        messagebox.showinfo("Максимальная глубина рекурсии", f"Максимальная глубина рекурсии: {recursion_limit}")

    # Создание графического интерфейса
    root = tk.Tk()
    root.title("Генератор Кривой Серпинского")

    tk.Label(root, text="Введите глубину фрактала:").pack(pady=5)
    depth_entry = tk.Entry(root)
    depth_entry.pack(pady=5)

    tk.Button(root, text="Сгенерировать кривую", command=on_generate).pack(pady=5)
    tk.Button(root, text="Показать глубину рекурсии", command=show_recursion_limit).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    run_program()