# if 5 > 2
#   print("yes")

# n = int("hello") # value error

# try:
#     age = int(input("Enter your age: "))
#     print("You are" + str(age) + " years old")
# except: ValueError:
#     print("Please enter a valid age")

# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     result = a / b
#     print(result)
# except ValueError:
#     print("Введено не число")
# except ZeroDivisionError:
#     print("На 0 ділити неможна ")

# try:
#     number = int(input("Please enter a number: "))
# except ValueError:
#     print("Please enter a number")
# else:
#     print("Квадрат від числа: ", number ** 2)


#try:
#    number = int(input("Enter a number: "))
#    print(100 / number)
#except ValueError:
#    print("Please enter a number")
#except ZeroDivisionError:
#    print("Please enter not 0")
#finally:                # Чим ми закінчуєу в будь якому випадку
#    print("End of the program")

#while True:
#    try:
#        grade = int(input("Enter your grade 1 - 12: "))
#        if grade < 1 or grade > 12:
#            raise ValueError("Grade must be between 1 and 12")
#        print(f'Your grade is {grade}')
#        break
#    except ValueError as error:
#        print(f'Error: {error}')

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print("Please enter an integer.")
# count = int(input("Please enter a number: "))
# print(f"Кількість {count}")


#def input_grade():
#    while True:
#        try:
#            grade = int(input("Enter your grade 1 - 12: "))
#            if grade > 12 or grade < 1:
#                raise ValueError("Grade must be between 1 and 12")
#            return grade
#        except ValueError as error:
#            print(error)
#
#grade = input_grade()
#print(f"Your grade is: {grade}")


#students = ["Anna", "Ivan", "Sophie"]
#try:
#    index = int(input("Please enter the index of the student: "))
#    print(students[index])
#except ValueError:
#    print("Please enter a valid index")
#except IndexError:
#    print("Елемента з таки індексом не існує")

#price = {
#    "apple": 50,
#    "banana": 70,
#    "mango": 50,
#}
#product = input("Please enter the product name: ")
#try:
#    print(f'Ціна: {price[product]}')
#except KeyError:
#    print("Такого товару немає")

# price = price.get(product, "немає у навності")
# print(price)

#try:
#    with open("data.txt", "r", encoding="utf-8") as file:
#        data = file.read()
#        print(data)
#except FileNotFoundError:
#    print("File not found")


#line = 'Anna;60'
#
#parts = line.strip().split(';')
#if len(parts) != 2:
#    print("Error")
#else:
#    name = parts[0]
#    grade = parts[1]
#
#    try:
#        score = int(grade)
#        if score < 0 or score > 100:
#            raise ValueError("Score out of range")
#    except ValueError as error:
#        print(f"Error  {error}")
#    else:
#        print(f"Запис правильний {name}: {score} балів")


lines = [
    'Anna;90',
    'Ivan;11',
    'Matvey;99'

]
for line_number, line in enumerate(lines, start=1):
    parts = line.strip().split(';')
    if len(parts) != 2:
        print(f"Рядок №{line_number}: пропущено через неправельний формат\n{line}")
        continue
    name = parts[0]
    grade = int(parts[1])
    try:
        grade = int(grade)
    except ValueError:
        print(f'Рядок №{line_number}, пропущено: бал е є числом ')
        continue
    print(f"Правильний запис: {name}, {grade}")
    
