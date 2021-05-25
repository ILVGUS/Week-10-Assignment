# Jennifer Adams
# CIS245-T301
# May 23, 2021
#
# Python program that collects directory input and a file name from user 
# and verifies existence of directory, then prompts user for name, address
# and phone number, prints the information in a comma separated line which 
# is stored to the filename they chose in the directory they specified
# and is then read by the program and displayed to user for verification.
#
# import the OS library. 
import os.path

# Introduce concept to user.
print("User Information File Building Tool")
print("\nLet's use a directory and filename of your choosing to store some"
" contact information.")

# Gather file name as input from user and assign to variable.
filename = input("\nWhat would you like to name your file? (ex: favorite_cats.txt): ")

# While loop to test for existence of directories.
while True:

    # Gather directory from user and assign to a variable.
    user_directory = input("\nWhich directory would you like to save this file to?: ")
    # Let user know we're checking the validity of the directory.
    print("Let's see if that directory exists first. . .")

    # If the directory is not able to be found. . . 
    if not os.path.exists(user_directory):
        # Notify user and have them try until they pick a valid directory.
        print("\nChosen directory does not exist!")

    # If the directory was valid. . . 
    else:
        # Let the user know. . .
        print("\nChosen directory exists!")
        # And exit the loop.
        break
# Gather information for the file from the user.
user_name = input("\nPlease enter your name: ")
user_address = input("Please enter your address: ")
user_phone = input("Please enter your phone number (ex: (xxx)xxx-xxxx): ")

# Place this input into a list.
join_list = [user_name, user_address, user_phone]

# Use .join to format the list into a comma separated string.
formatted_info = ', '.join(join_list)

# Use with to create a file for the user in their specified directory.
with open(os.path.join(user_directory, filename), 'w') as file_object:
    # Place the user's information into the file.
    file_object.write(formatted_info)

    # Let the user know their information has been saved, and let them see where it saved to.
    print("\nFile saved to", user_directory)

# Let user know their information will be displayed for verification.
print("\nYour user information file reads as follows:\n")

# Open the file from the directory the user chose to save it to.
with open(os.path.join(user_directory,filename), 'r') as file_object:
    for line in file_object:
        # And display the information to the user.
        print(line)