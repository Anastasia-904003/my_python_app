def add(a, b):
    return a + b

if __name__ == "__main__":
    try:
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Сума: {add(x, y)}")
    except ValueError:
        print("Введіть числа!")