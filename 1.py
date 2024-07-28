def generate_password(n):
    if not 3 <= n <= 20:
        return "Число должно быть от 3 до 20."
    password = ""
    used_numbers = set()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0 and i not in used_numbers and j not in used_numbers:
                password += str(i) + str(j)
                used_numbers.add(i)
                used_numbers.add(j)
    return password


while True:
    try:
        n = int(input("Введите число из первой каменной вставки (от 3 до 20): "))
        if 3 <= n <= 20:
            password = generate_password(n)
            print(f"{n} - {password}")
            break
        else:
            print("Некорректное число. Введите число от 3 до 20.")
    except ValueError:
        print("Некорректный ввод. Введите число.")

