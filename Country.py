# Earl Miller CIS261 Country Lab

def display_menu():
    print("COMMAND MENU")
    print("view - country name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")
    print()

def display_codes(countries):
    code = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        code_line += code + ""
    print(code_line)

def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")

def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

def delete(countried):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
         name = countries.pop(code)
         print(f"{name} was deleted.\n")
    else:
         print("There is no country with that code.\n")

def main():
    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico"}

    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command =="add":
            add(countries)
        elif command == "del":
            delete(coutries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")