# #1
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     opt = input("Введіть операцію: ")
#     o = "opt"
#     if opt =="/":
#         print(a/b)
#     if opt =="*":
#         print(a*b)
#     if opt =="-":
#         print(a-b)
#     if opt =="+":
#         print(a+b)
# except ValueError:
#     print("Введено не число")
# except ZeroDivisionError:
#     print("На 0 ділити неможна ")
#
# #2
# while True:
#    try:
#        grade = int(input("Enter your grade 1 - 12: "))
#        if grade < 1 or grade > 12:
#            raise ValueError("Grade must be between 1 and 12")
#        print(f'Your grade is {grade}')
#        break
#
#    except ValueError as error:
#        print(f'Error: need to input a normal number')

#3
students = [
    'Vin',
    '$vin',
    's1mple'
]

# Словник предметів і оцінок
stg = {
    'math': 90,
    'science': 90,
    'biology': 90,
    'chemistry': 90,
    'geography': 90,
    'pravo': 90,
    'history': 90
}

print("1 — учень за індексом")
print("2 — оцінка за назвою предмета")

try:
    mch = int(input("Оберіть (1 або 2): "))

    if mch == 1:
        try:
            index = int(input("Введіть індекс учня: "))
            if index < 0 or index >= len(students):
                raise IndexError
            print(f"Знайдено учня: {students[index]}")
        except ValueError:
            print("Помилка: введено нечисловий індекс учня.")
        except IndexError:
            print("Помилка: учня з таким індексом немає.")
    elif mch == 2:
        try:
            sub = input("Введіть назву предмета: ").strip().lower()
            if sub not in stg:
                raise KeyError
            print(f"Предмет: {sub}, Оцінка: {stg[sub]}")
        except KeyError:
            print("Помилка: такого предмета немає в словнику.")
    else:
        print("Помилка: невідомий пункт меню, будь ласка, оберіть 1 або 2.")
except ValueError:
    print("Помилка: введено нечислове значення для вибору пункту меню.")

