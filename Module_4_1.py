from true_math import divide as true_math
from fake_math import divide as fake_math

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

result1 = true_math(first, second)
result2 = fake_math(first, second)

print(f'Результат деления способом true_math: {result1}')
print(f'Результат деления способом fake_math: {result2}')
