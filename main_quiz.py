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

# main_quiz.py - Main logic for the quiz


import random
import os
import threading
import time
from quiz_data import quiz_data

timer_display = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer():
    global timer_display
    total_seconds = 90 * 60  # 90 minutes in seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f'{mins:02d}:{secs:02d}'
        time.sleep(1)
        total_seconds -= 1
    timer_display = "00:00"
    print("\nTime's up!")
    os._exit(0)

def run_quiz():
    global timer_display
    correct_answers = 0
    total_questions = len(quiz_data)
    selected_questions = random.sample(quiz_data, total_questions)

    timer_thread = threading.Thread(target=countdown_timer)
    timer_thread.daemon = True
    timer_thread.start()

    for idx, item in enumerate(selected_questions, 1):
        while True:
            clear_screen()
            print(f"Time Remaining: {timer_display}\n")
            print(f"Question {idx}: {item['question']}")
            for choice in item['choices']:
                print(choice)
            print("E. Exit Quiz")
            user_answer = input("Your answer (A/B/C/D/E): ").strip().upper()

            if user_answer == 'E':
                print("You chose to exit the quiz.")
                return

            if user_answer in ['A', 'B', 'C', 'D']:
                break

        if user_answer == item['answer']:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was {item['answer']}.")

        time.sleep(2)  # Pause for 2 seconds before moving to the next question

    incorrect_answers = total_questions - correct_answers
    score_percentage = (correct_answers / total_questions) * 100

    print("\nQuiz Results:")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")
    print(f"Score Percentage: {score_percentage:.2f}%")

    if score_percentage >= 70:
        print("Congratulations! You passed the quiz.")
    else:
        print("You failed the quiz. Better luck next time!")

if __name__ == "__main__":
    run_quiz()
