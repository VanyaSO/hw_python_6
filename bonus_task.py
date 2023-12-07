Seconds_in_day = 24 * 60 * 60
Seconds_in_hour = 3600
Seconds_in_minute = 60

# Ask how much time has passed from the user in seconds
passed_time = int(input("How much time has passed, enter in seconds: "))

#if the user enters number <0 or >1 day, stop executing the code
if passed_time < 0 or passed_time > Seconds_in_day: 
    print("Enter another value")
    exit()    

# Сalculate how many time left
left_time = Seconds_in_day - passed_time

# Сalculate how many hours, minutes, seconds, left
left_hours = left_time // Seconds_in_hour
left_minutes = (left_time % Seconds_in_hour) // Seconds_in_minute
left_seconds = left_time % Seconds_in_minute

# Ask what want to see result user / output option
output_option = input("What do you want to see result?: 1(all time) 2(only hours) 3(only minutes) 4(only seconds)")

match output_option:
    case "1": print(f"Left until the end of the day: {left_hours} hours/{left_minutes} minutes/{left_seconds} seconds")
    case "2": print(f"Left until the end of the day: {left_hours} hours")
    case "3": print(f"Left until the end of the {left_time // 60} minutes")
    case "4": print(f"Left until the end of the day: {left_time} seconds")
    case _: print("Error")





