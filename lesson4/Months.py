month = ["January", "February", "March", "April",
         "May", "June", "July", "August", "September",
         "October", "November", "December"]
error = "You made a mistake, repeat with numbers from 1 to 12"

try:
    number = int(input("Please, enter a number from 1 to 12: "))
    if 0 < number < 13:
        print(month[number - 1])
    else:
        print(error)
except ValueError:
    print(error)
