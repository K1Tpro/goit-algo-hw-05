def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Key Error"
        except IndexError:
            return "Please enter the name."

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name} is {contacts.get(name)}"
    else:
        return f"There are no {name} in your contacts"


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return f"There are no {name} in your contacts. Type add for the new contact"


@input_error
def all_contacts(contacts):
    for i in contacts:
        print(f"{i}: {contacts[i]}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "update":
            print(change_contact(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()