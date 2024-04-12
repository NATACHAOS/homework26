print('Высокосный ли год?')
message = int(input("Напишите год и нажмите Enter: "))
if (message % 4 == 0) and (message % 100 != 0) or (message % 400 == 0):
    print('ГОД ВЫСОКОСНЫЙ')
else:
    print('Год не высокосный')
