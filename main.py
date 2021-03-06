from user_functions import *

while True:
    print("1. Add New User\n"
          + "2. Get All Users\n"
          + "3. Search\n"
          + "4. Update User By Id\n"
          + "5 if you want exit"
          )
    menu_flag = int(input("Type your choose: "))
    if menu_flag == 1:
        user_add()
    elif menu_flag == 2:
        try:
            get_all()
        except UnboundLocalError:
            print("incorrect data")
    elif menu_flag == 3:
        what_to_search = input('By Which Parametr you want to search: ')
        search_str = input('Search: ')
        search_by(search_str, what_to_search)
    elif menu_flag == 4:
        update_user()
    elif menu_flag == 5:
        break
