"""
Author: Jose Sanchez-Capo  
Email: josesanchezcapo@gmail.com  

Disclaimer:  
The information provided in this quiz is based on publicly available documentation from the official AWS website (https://aws.amazon.com).  
This quiz is offered "as is" for educational purposes only, with no guarantees of accuracy, completeness, or suitability for any purpose.  
For the most accurate and up-to-date information, please refer to the official AWS documentation.  

Feedback:  
If you encounter any errors, have suggestions for improvements, or would like to modify this quiz to better fit your needs,  
please feel free to provide feedback. Your input is greatly appreciated and helps improve the quality of this resource.  
"""

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    clear_screen()
    print("AWS Quiz Application")
    print("====================")
    print("1. Start Quiz")
    print("2. View Past Results")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice
