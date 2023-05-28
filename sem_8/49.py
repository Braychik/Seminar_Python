from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = str(all_data[-1].split()[0])
            return all_data
    return []

def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number

def add_record():
    info = ' '.join(get_new_number())
    with open(file_base, "a", encoding="utf-8") as file:
         file.write(f'{info}\n')

def Search_record():
    search_data = exist_contact(0, input("Введите данные для поиска: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("The data is not correct!")


def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def change_contact(data_tuple):

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def data_collection(num):

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer

def del_contact():

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")


def main_menu():
    play = True
    while play:
        read_records()

        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_record()
            case "3":
                Search_record()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
               pass
            case "7":
                play = False
            case _:
                print("Try again!\n")

def edit_menu():

    add_dict = {"1": "surname", "2": "name", "3": "phone number"}

    show_all()
    record_id = input("Enter the record id: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. phone number\n"
                           "4. exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")

main_menu()