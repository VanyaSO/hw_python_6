# Користувач вводить із клавіатури номер дня тижня (1-7). 
# Необхідно вивести на екран назву дня тижня. Наприклад, якщо 1, то на екрані напис "понеділок", 2 — "вів-торок" і т.д.

number = int(input("Enter the week number from 1-7: "))

match number: 
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wensday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Error")
    
