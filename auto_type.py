from pynput.keyboard import Key, Controller
import time

keyboard= Controller()

def auto(n):
    time.sleep(5)
    for i in n.split("\n"):
        keyboard.type(i)
        keyboard.press(Key.enter)
        time.sleep(0.01)

# code to auto type in your editor
# ***For proper indentation comment your code inside the string.***
n='''
# import os

# def file_system_operations() -> dict:
#     current_directory = os.getcwd() 
#     files_in_directory = os.listdir(current_directory)

#     # Use /tmp/ folder for creating 'new_folder' to avoid permission issues
#     temp_directory = '/tmp/new_folder'
#     if not os.path.exists(temp_directory):
#         os.mkdir(temp_directory)
#         msg = "new_folder created successfully in /tmp/."
#     else:
#         msg = "new_folder already exists in /tmp/."

#     result = {
#         'current_directory': current_directory,
#         'files_in_directory': files_in_directory,
#         'confirmation_message': msg
#     }

#     return result

# print(file_system_operations())
'''
auto(n) 
