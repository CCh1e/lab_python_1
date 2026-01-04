print("\n--- Завдання 2 ---")

a = 5
b = 80

sum_squares = 0  # Сума квадратів
count = 0        # Кількість чисел

# Цикл від 5 до 80 включно
for i in range(a, b + 1):
    sum_squares += i ** 2
    count += 1

average = sum_squares / count

print(f"Діапазон: [{a}, {b}]")
print(f"Сума квадратів: {sum_squares}")
print(f"Кількість чисел: {count}")
print(f"Середнє арифметичне квадратів: {average:.2f}")
