import sys, os

#colors
RED = '\033[31m'
RESET = '\033[0m' 
def red_font(s):
    return RED + str(s) + RESET

def help():
    print(f"Press {red_font('e')} to exit")
    print(f"Press {red_font('a')} to add a contact")
    print(f"Press {red_font('d')} to delete a contact")
    print(f"Press {red_font('s')} to save data to file")
    print(f"Press {red_font('l')} to load data from file")  
    print(f"Press {red_font('v')} to view all your contacts")
    print(f"Press {red_font('f')} to find the phone number of a given name")
    print(f"Press {red_font('u')} to update the phone number of a given name")
    print(f"Press {red_font('h')} to show help message")

def welcome():
    message = f"Welcome to {red_font(NAME)}'s phonebook app"
    n = len(message) - len(NAME)
    print("-"*n)
    print(message)
    print("-"*n)
    help()

def load(filename):
    phonebook = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                k, v = line.strip().split(",")
                phonebook[k] = v
            return phonebook
    except FileNotFoundError:
        print(f"File {filename} not found. A new file will be created.")
        open(filename, 'w').close()
        return phonebook
    except Exception as e:
        print(f"An error occurred: {e}")
    return phonebook

def save(phonebook, filename):
    with open(filename, "w") as f:
        for k, v in phonebook.items():
            f.write(k + "," + v + "\n")
    print(f"Contacts saved to {filename}.")

def add(phonebook,filename):
    name = input("Please enter the name: ")
    number = input("Please enter the number: ")
    if not number or not name:
        print("Error", "Name and number cannot be empty.")
    elif number in phonebook.values():
        print(f"The number {number} already exists for another contact.")
    else:
        phonebook[name] = number
        save(phonebook, filename)

def update(phonebook,filename):
    name = input("Please enter the name: ").strip()
    number = input("Please enter the number: ")
    if not name or not number:
        print("Error", "Name and number cannot be empty.")
        return
    if name in phonebook:
        if number in phonebook.values():
            print(f"The number {number} already exists for another contact.")
        else:
            phonebook[name] = number
            save(phonebook, filename)
            print(f"Added {name} with number {number}.")
    else:
        while True:
            x = input("The name you entered doesn't exist. Do you want to add it? (y/n): ").lower()
            if x == 'y':
                if number in phonebook.values():
                    print(f"The number {number} already exists for another contact.")   
                else:
                    phonebook[name] = number
                    save(phonebook, filename)
                    print(f"Added {name} with number {number}.")
                break
            elif x == 'n':
                print("No changes made.")
                break
            else:
                print("Please enter a valid option (y/n).")

def find(phonebook):
    name = input("Please enter the name: ")
    if not name:
        print("Error: Name cannot be empty.")
        return
    if name in phonebook:
        print(f"{name}: ", phonebook[name])
    else:
        print(f"Can't find {name} in phonebook")

def delete(phonebook,filename):
    name = input("Please enter the name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    if name in phonebook:
        del phonebook[name]
        save(phonebook, filename)
    else:
        print(f"Can't delete {name} in phonebook")

def view(phonebook):
    for k, v in phonebook.items():
        spaces = 30 - len(k)
        print(f"{k}{' ' * spaces}: {v}")

def main(): 
    global NAME
    NAME = input("Enter your name: ")
    phonebook = {}
    global filename
    filename = input("Enter the filename to save your contacts: ")
    phonebook=load(filename)
    
    welcome()
    while True:
        choice = input("> ").lower()
        if choice == "e":
            exit()
        elif choice == "l":
            phonebook = load(filename)
        elif choice == "s":
            save(phonebook, filename)
        elif choice == "a":
            add(phonebook,filename)
        elif choice == "f":
            find(phonebook)
        elif choice == "u":
            update(phonebook,filename)
        elif choice == "d":
            delete(phonebook,filename)
        elif choice == "v":
            view(phonebook)
        elif choice == "h":
            help()
        else:
            print("Invalid input.")
            help()

if __name__ == "__main__":
    main()
