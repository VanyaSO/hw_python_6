# Користувач вводить із клавіатури число. 
# Якщо число більше нуля, потрібно вивести напис "Number is positive", 
# якщо менше нуля — "Number is negative", 
# якщо дорівнює нулю — "Number is equal to zero"

number = int(input("Enter please number: "))

if number > 0 :
    print("Number is positive")
elif number < 0 : 
    print("Number is negative")
else :
    print("Number is equal to zer")