from builtins import input

print("Сколько тебе лет?", end=" ")
age = input()
print('Каков твой рост?', end=" ")
height = input()
print('Сколько ты весишь?', end=" ")
weight = input("--> ")

print(f"Итак, тебе {age} лет, в тебе {height} см роста и {weight} кг веса.")

print("Сложите два числа: ")
print("Введите первое число:", end=' ')
x = int(input())
print("Введите второе число:", end=' ')
y = int(input())
print(f"Вы ввели {x} и {y}, сумма равна {x+y}")