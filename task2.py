# Користувач вводить із клавіатури номер місяця (1-12). 
# Необхідно вивести на екран назву місяця. 
# Наприклад, якщо 1, то на екрані напис "січень", 2 — "лютий" і т.д.

number = int(input("Enter the month number from 1-12: "))

match number: 
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("May")
    case 6: print("June")
    case 7: print("July")
    case 8: print("August")
    case 9: print("September")
    case 10: print("October")
    case 11: print("November")
    case 12: print("December")
    case _: print("Error")