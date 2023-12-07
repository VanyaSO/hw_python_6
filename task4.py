# Користувач вводить два числа. 
# Необхідно визначити, чи ці числа є рівними і,
# якщо ні, вивести їх на екран у порядку зростання.

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number == second_number :
    print("Numbers are equal")
elif first_number < second_number:
    print(first_number, second_number)
else :
    print(second_number, first_number)