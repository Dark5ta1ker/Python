def count():
    low = float(input("Введите нижний предел\n"))
    high = float(input("Введите верхний предел\n"))

    k = 1  # номер итерации
    i = 1  # числитель дроби

    while True:
        n = 2 ** k
        current = i / n
        print(f"| {k} | {i} | {n} | {current} |")

        if current > high:
            i = i * 2 - 1
        elif current < low:
            i = i * 2 + 1
        else:
            print(f"Значение попало в диапазон [{low}, {high}]:")
            print(f"| {k} | {i} | {n} | {current} |")
            break

        k += 1  
count()
    
