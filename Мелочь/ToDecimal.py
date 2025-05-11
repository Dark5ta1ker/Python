
def math (start):
    f = 0
    k = 0
    for i in reversed(start):
        f += (2 ** k) * int(i)
        k += 1
    return f
print(math(input("Введите число: ")))