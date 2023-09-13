n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number**3)

print("Список кубов введенных чисел:", numbers)
summa = sum(numbers)
proizvedenie = 1
for number in numbers:
    proizvedenie *= number

print("Сумма элементов списка:", summa)
print("Произведение элементов списка:", proizvedenie)
print("Список в обратном порядке:", numbers[::-1])