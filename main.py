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

from menu import display_menu
from quiz import start_quiz
from results import save_result, view_past_results


def main():
    while True:
        choice = display_menu()

        if choice == "1":
            result = start_quiz()
            save_result(result)
            print("Quiz Completed!")
            print(f"Your Score: {result['score']:.2f}% - {result['status']}")
            input("Press Enter to return to the menu...")
        elif choice == "2":
            view_past_results()
            input("Press Enter to return to the menu...")
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()