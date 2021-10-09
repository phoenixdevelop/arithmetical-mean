num_1 = int(input("Введите значение 1: "))
value_1 = int(input("Введите колчество: "))
num_2 = int(input("Введите значение 2: "))
value_2 = int(input("Введите колчество : "))
num_3 = int(input("Введите значение 3,  если такого нет, ввести 0: "))
value_3 = int(input("Введите колчество, если такого нет, ввести 0 : "))
num_3 = int(input("Введите значение 4,  если такого нет, ввести 0: "))
value_4 = int(input("Введите колчество, если такого нет, ввести 0 : "))
result = (num_1 * value_1 + num_2 * value_2 + num_3 * value_3 + num_3 * value_3 ) / (value_1 + value_2 + value_3 + value_4)
print ("Среднее арифметическое" , result)
if result >= float(4.2):
    print("Хорший балл")
else:
    print('Плохой балл, потсупить будет сложно')
