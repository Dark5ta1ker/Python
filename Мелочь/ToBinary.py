start = int(input("Введите число: "))
finish = []

def math():
    n = start
    while n > 0:
        finish.append(n % 2)
        n = n // 2
    finish.reverse()
    return "".join(str(bit) for bit in finish)

print(math())
