def ancient_cipher(n):

  if 1 <= n <= 20:
    result = ""
    for i in range(1, 10):
      for j in range(i, 10):
        if (i + j) != 0 and n % (i + j) == 0:
          result += str(i) + str(j)
    return result

while True:
  n = int(input("Введите число из первой каменной вставки (от 1 до 20, или другое число для выхода): "))

  if 1 <= n <= 20:
    password = ancient_cipher(n)
    print(f"Пароль для числа {n}: {password}")
  else:
    break
