from json import loads, dump, dumps
from tkinter import Button, Entry, font, Label, INSERT
from canvas import root, frame
from gui_health_system.helpers import clean_screen


# With this function we are getting the information for the users from our Database
def get_users_data():
    info_data = []

    # here we are opening the users_information file from the Database folder for reading
    with open("C:\\Users\\IvayloveAnna\\PycharmProjects\\GUIproject\\Database\\users_information.txt", "r") \
            as users_file:
        for line in users_file:
            # here we are taking the data from the users_information file as a string, and it will convert it in a
            # dictionary using json
            info_data.append(loads(line))

    return info_data


# With this function we are getting the information for the users health state (illnesses, blood type, etc.) from
# our Database
def get_user_health_state():
    health_state_data = []
    with open("C:\\Users\\IvayloveAnna\\PycharmProjects\\GUIproject\\Database\\users_health_state.txt",
              "r") as users_file:
        for line in users_file:
            health_state_data.append(loads(line))

    return health_state_data

    # for data in health_state_data:
    #     for key, value in data.items():
    #         for inner_value in value.values():
    #             if inner_value != illnesses_box.get():
    #                 return True
    #             return False


# This function create and  visualize the login and register buttons
def render_entry():
    # attaching and styling the register button to the root
    register_button = Button(
        root,
        text="Register",
        # background color
        bg="green",
        # font color
        fg="white",
        # removing the border of the window button
        borderwidth=0,
        # setting the size of the window button
        width=20,
        height=3,
        # this command is used when we click the register button to execute the function register and clean all the
        # data from the canvas and open the register menu
        command=register,
    )

    # set the font to the register button text
    register_button['font'] = my_font

    # attaching and styling the login button to the root
    login_button = Button(
        root,
        text="Login",
        # background color
        bg="blue",
        # font color
        fg="white",
        # removing the border of the window button
        borderwidth=0,
        # setting the size of the window button
        width=20,
        height=3,
        # this command is used when we click the login button to execute the function login and clean all the
        # data from the canvas and open the login menu
        command=login,
    )

    # set the font to the login button text
    login_button['font'] = my_font

    # attaching and styling the check patient button to the root
    check_patient_button = Button(
        root,
        text="Check Patient",
        bg="red",
        borderwidth=0,
        width=20,
        height=3,
        # this command is used when we click the check patient button to execute the function check patient and
        # clean all the data from the canvas and open the check patient menu
        command=check_patient,
    )

    # set the font to the check patient button text
    check_patient_button['font'] = my_font

    # attaching to the frame and creating the register button on the screen
    frame.create_window(350, 260, window=register_button)
    # attaching to the frame and creating the login button on the screen
    frame.create_window(350, 350, window=login_button)
    frame.create_window(350, 440, window=check_patient_button)
    # attaching to the frame and creating the logo of the program
    frame.create_text(350, 150, text="World HealthCare Database System", font=("High Tower Text", 20))
    frame.create_text(350, 100, text="Welcome to", font=("High Tower Text", 20))


# this function clear the data from the canvas after we click the login button and entering the login menu
def login():
    clean_screen()

    # creating the text in the login menu
    frame.create_text(100, 50, text="UCN:", font=("Rockwell", 11))
    frame.create_text(100, 100, text="Password:", font=("Rockwell", 11))

    # attaching the boxes to the canvas at the login menu
    frame.create_window(200, 50, window=UCN_box)
    frame.create_window(200, 100, window=password_box)

    # creating the login button in the login menu
    logging_button = Button(
        root,
        text="Login",
        bg="green",
        fg="white",
        borderwidth=0,
        command=logging
    )

    back_button = Button(
        root,
        text='Back',
        bg="white",
        fg="black",
        borderwidth=0,
        command=back_to_main_page
    )

    # set the font to the login button text
    logging_button['font'] = my_font
    back_button['font'] = my_font
    # attaching the login button to the canvas in the login menu
    frame.create_window(250, 150, window=logging_button)
    frame.create_window(40, 550, window=back_button)


# This function creating the patient health state window where we are filling the illnesses, blood type, etc.
def logging():
    if logging_validation():
        clean_screen()
        frame.create_text(100, 50, text="Illnesses:", font=("Rockwell", 11))
        frame.create_text(100, 100, text="Blood Type:", font=("Rockwell", 11))

        frame.create_window(300, 50, window=illnesses_box, width=300, height=20)
        frame.create_window(300, 100, window=blood_type_box, width=300, height=20)
    else:
        frame.create_text(160, 200, text="Invalid UCN or password", fill="red")

    save_button = Button(
        root,
        text="Save",
        bg="green",
        fg="white",
        borderwidth=0,
        command=save_user_health_state,
    )

    back_button = Button(
        root,
        text='Back',
        bg="white",
        fg="black",
        borderwidth=0,
        command=back_to_login_menu
    )

    frame.create_window(300, 250, window=save_button)
    frame.create_window(40, 550, window=back_button)

    save_button['font'] = my_font
    back_button['font'] = my_font


# this function validate the input data from login fields
def logging_validation():
    info_data = get_users_data()

    user_UCN = UCN_box.get()
    user_password = password_box.get()

    for index in range(len(info_data)):
        UCN = info_data[index]["UCN"]
        password = info_data[index]["password"]

        if UCN == user_UCN and password == user_password:
            return True

    return False


# This function saves the health state data of the users in the database as a dictionary
def save_user_health_state():
    health_state_data = get_user_health_state()
    current_user_UCN = UCN_box.get()

    health_state_dictionary = {
        current_user_UCN: {"illnesses": illnesses_box.get(), "blood_type": blood_type_box.get()},
    }

    if valid_user_data(health_state_dictionary):
        with open("C:\\Users\\IvayloveAnna\\PycharmProjects\\GUIproject\\Database\\users_health_state.txt",
                  "a") as users_file:
            # users_file.write(dumps(health_state_dictionary))
            # for line in users_file:
            #     (key, value) = line.split()
            #     dump(health_state_dictionary[key], value)
            # if health_state_dictionary[current_user_UCN]:
            #     health_state_dictionary.update(health_state_dictionary)

            dump(health_state_dictionary, users_file)
            users_file.write('\n')

    # for element in health_state_data:
    #     if not element.values():
    #         frame.create_text(300, 300, text="must be fill", fill="green")
    #     else:
    #         frame.create_text(300, 300, text="Add data successfully", fill="green")
    # for data in health_state_data:
    #     for key, value in data.items():
    #         for inner_value in value.values():
    #             if inner_value != illnesses_box.get():
    #                 with open(
    #                         "C:\\Users\\IvayloveAnna\\PycharmProjects\\GUIproject\\Database\\users_health_state.txt",
    #                         "a") as users_file:
    #                     dump(health_state_dictionary, users_file)
    #                     users_file.write('\n')


# this function validates if we have filled all the fields in health user state (illnesses, blood type and etc.)
def valid_user_data(info):
    for element in info.values():
        for curr_element in element.values():
            if not curr_element.strip():
                frame.create_text(300, 300, text="You have to fill all fields!", fill="red", tags="error")
                return False

    frame.delete("error")
    frame.create_text(300, 300, text="Add data successfully! Please back to main screen", fill="green")
    return True


# this function clear the data from the canvas after we click the register button and entering the register menu
def register():
    clean_screen()

    # creating the text in the register menu
    frame.create_text(100, 50, text="First name:", font=("Rockwell", 11))
    frame.create_text(100, 100, text="Last name:", font=("Rockwell", 11))
    frame.create_text(100, 150, text="UCN:", font=("Rockwell", 11))
    frame.create_text(100, 200, text="Password:", font=("Rockwell", 11))

    # attaching the boxes to the canvas at the register menu
    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=UCN_box)
    frame.create_window(200, 200, window=password_box)

    # creating the register button in the register menu
    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        command=registration
    )

    back_button = Button(
        root,
        text='Back',
        bg="white",
        fg="black",
        borderwidth=0,
        command=back_to_main_page
    )

    # set the font to the register button text
    register_button['font'] = my_font
    back_button['font'] = my_font
    # attaching the register button to the canvas in the register menu
    frame.create_window(300, 250, window=register_button)
    frame.create_window(40, 550, window=back_button)


# this function collect the user data in dictionary
def registration():
    info_dictionary = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "UCN": UCN_box.get(),
        "password": password_box.get(),
    }

    # here we are appending the information of a new user to our database
    if validate_registration(info_dictionary):
        with open("C:\\Users\\IvayloveAnna\\PycharmProjects\\GUIproject\\Database\\users_information.txt",
                  "a") as users_file:
            dump(info_dictionary, users_file)
            users_file.write('\n')


# this function validate the input data from registration fields
def validate_registration(info):
    for element in info.values():
        if not element.strip():
            frame.create_text(300, 300, text="You have to fill all fields", fill="red", tags="error")
            return False

    # if the for loop return True it will delete the error message with tag "error"
    frame.delete("error")

    info_data = get_users_data()

    # here we are checking if there is a person with the same UCN when a person is registrate himself
    for record in info_data:
        if record["UCN"] == info["UCN"]:
            frame.create_text(300, 300, text="User with this UCN already exists!", fill="red", tags="error")
            return False

    frame.delete("error")
    frame.create_text(300, 300, text="Create account successfully! Please back to main screen", fill='green')
    return True


# this function clear the data from the canvas after we click the check patient button and entering the
# check patient menu
def check_patient():
    clean_screen()

    # creating the text in the check patient menu
    frame.create_text(350, 100, text='Patient UCN:', font=("Rockwell", 20))

    # attaching the box to the canvas at the check patient menu
    frame.create_window(350, 150, window=patient_UCN_box, width=200, height=25)

    # creating the see patient database button in the check patient menu
    see_patient_database_button = Button(
        root,
        text="See patient database",
        bg="green",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=show_patient_data,
    )
    # creating the back button in the check patient menu
    back_button = Button(
        root,
        text='Back',
        bg="white",
        fg="black",
        borderwidth=0,
        command=back_to_main_page
    )

    # set the font to the see patient database button text
    see_patient_database_button['font'] = my_font
    back_button['font'] = my_font

    # attaching the see patient database button and back button to the canvas in the check patient menu
    frame.create_window(350, 250, window=see_patient_database_button)
    frame.create_window(40, 550, window=back_button)


# this function clear the data from the canvas after we click the see patient database button and entering the
# patient database menu
def show_patient_data():
    clean_screen()
    data = get_user_health_state()
    key = patient_UCN_box.get()
    print(key)
    for el in data:
        for curr_el in el:
            if key == curr_el:

                frame.create_text(300, 10, text=el.values())

    # with open("C:\\Users\\IvayloveAnna\\PycharmProjects\\GUIproject\\Database\\users_information.txt",
    #           "r") as users_file:
    #     Label(root, text=users_file.read()).pack()

    # file = open("users_health_state.txt")
    # data = file.read()
    # file.close()
    # results = Label(root, text=data)
    # results.grid(row=1, column=1)

    back_button = Button(
        root,
        text='Back',
        bg="white",
        fg="black",
        borderwidth=0,
        command=back_to_check_patient_menu,
    )

    frame.create_window(40, 550, window=back_button)
    back_button['font'] = my_font


# This function is used to back to the main screen of the program
def back_to_main_page():
    clean_screen()
    render_entry()


# This function is used to back to patient menu of the program
def back_to_check_patient_menu():
    clean_screen()
    check_patient()


# This function is used to back to login menu of the program
def back_to_login_menu():
    clean_screen()
    login()


# creating the input fields for the first name, last name, username, password, illnesses, blood type, patient UCN
first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
UCN_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")
illnesses_box = Entry(root, bd=0)
blood_type_box = Entry(root, bd=0)
patient_UCN_box = Entry(root, bd=0)

# define font for the buttons
my_font = font.Font(family="High Tower Text")
