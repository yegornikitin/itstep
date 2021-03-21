import re

database = []
error = "Not correct input. Please, try one more time"


def add_new_member_name(input_name):
    name = re.findall(".", input_name)
    if name[0].isupper() == True:
        return input_name
    else:
        return error


def add_new_member_surname(input_surname):
    surname = re.findall(".", input_surname)
    if surname[0].isupper() == True:
        return input_surname
    else:
        return error


def add_new_member_mobile_phone(input_mobile_phone):
    if re.match("[+]{1}[3]{1}[8]{1}[0-9]{10}", input_mobile_phone) and len(input_mobile_phone) == 13:
        return input_mobile_phone
    else:
        return error


def add_new_member_email(input_email):
    while True:
        email = re.findall("@\w+.\w+", input_email)
        for i in email:
            if i == "@gmail.com":
                return input_email
        else:
            return error


while True:
    start_input = input("------------------------------\n"
                        "Please, choose what you want: \n"
                        "Print '1' - Add new member to the database \n"
                        "Print '2' - Show database \n"
                        "Print '3' - Exit \n")
    if start_input == "1":
        input_name = input("Please, enter a name: ")
        if add_new_member_name(input_name) == error:
            print(error)
            continue
        input_surname = input("Please, enter a surname: ")
        add_new_member_surname(input_surname)
        if add_new_member_surname(input_surname) == error:
            print(error)
            continue
        input_mobile_phone = input("Please, enter a mobile: ")
        add_new_member_mobile_phone(input_mobile_phone)
        if add_new_member_mobile_phone(input_mobile_phone) == error:
            print(error)
            continue
        input_email = input("Please, enter an email: ")
        add_new_member_email(input_email)
        if add_new_member_email(input_email) == error:
            print(error)
            continue
        new_member = (add_new_member_name(input_name),
                      add_new_member_surname(input_surname),
                      add_new_member_mobile_phone(input_mobile_phone),
                      add_new_member_email(input_email))
        database.append(new_member)
        print("New member was added")
        continue
    if start_input == "3":
        print("Thank for using program")
        exit()

    if start_input == "2":
        for i in database:
            print("Current database is: \n", i, end="\n")
        continue
    else:
        print("Not correct input")
