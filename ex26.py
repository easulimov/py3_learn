from sys import argv


def about_you():
    """Функция получает пользовательский ввод и печатает данные"""
    print("Сколько вам лет?", end=' ')
    age = input()
    print("Какого вы роста?", end=' ')
    height = input()
    print("Сколько вы весите?", end=' ')
    weight = input()

    print(f"Итак, вам {age} лет, ваш рост - {height} и ваш вес - {weight}.")


script, filename = argv


def file_open(file):
    txt = open(file)
    print(f"Вот ваш файл : {file}")
    print(txt.read())
    txt.close()


def txt_again_read():
    print("Снова укажите имя файла (для выхода нажмите 'q'):")
    try:
        file_again = input("> ")
        if file_again == "q":
            return
        txt_again = open(file_again)
        print(txt_again.read())
        txt_again.close()
    except FileNotFoundError:
        print("Имя файла указано не верно")
        txt_again_read()




print('Давайте попрактикуемся!')
print("""ВЫ должны знать об управляющих последовательностях с символом \\, которые 
      \\n управляют переносом строк и \\t отступами.""")

poem = """
\tДля счастья
мне совсем немного надо.
Хочу тебя \n я нежно обнимать.
Хочу всегда
я быть с тобою рядом
\n\t\tи никогда не отпускать!
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - (2 + 3)
print(f"Здесь должна быть пятерка: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# помните, что это еще один способ форматирования строки
print("Начиная с: {}".format(start_point))
# так же, как со строкой f""
print(f"У нас есть {beans} бобов, {jars} банок и {crates} ящиков.")

start_point = start_point / 10

print("Мы также можем сделать это таким образом:")
formula = secret_formula(start_point)
# простой способ применить список к форматируемой строке
print("У нас есть {} бобов, {} банок и {} ящиков.".format(*formula))

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Слишком много кошек! Мир обречен!")

if people > cats:
    print("Не так много кошек! Мир спасен!")

if people < dogs:
    print("Мир утоп в слюнях!")

if people > dogs:
    print("Мир сухой!")

dogs += 5

if people >= dogs:
    print("Людей больше или столько же, сколько собак.")

if people <= dogs:
    print("Людей меньше или столько же, сколько собак.")

if people == dogs:
    print("Людей столько же, сколько собак.")

about_you()

file_open(filename)

txt_again_read()
