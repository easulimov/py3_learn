# Импорт argv для передачи аргументов в сценарий
from sys import argv
# Разупаковка аргументов и присвоение переменным
script, filename = argv

# Открытие файла
txt = open(filename)

print(f"Содержимое файла {filename}:")
# Чтение файла и вывод на экран
print(txt.read())
print("Снова введите имя файла:")
# Приглашение на повтрный ввод имени файла
file_again = input("> ")
# Открытие файла и присвоение его имени новой переменной
txt_again = open(file_again)

# Чтение файла и вывод на экран
print(txt_again.read())
txt.close()
txt_again.close()