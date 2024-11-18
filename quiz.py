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

import time
import curses
import random
from datetime import datetime
from quiz_data import quiz_data


def start_quiz():
    """
    Starts the quiz and handles the quiz flow, including timing, user input, and scoring.

    The quiz consists of a series of questions, each with multiple choices. The user has a limited
    amount of time (90 minutes) to complete the quiz. The quiz ends either when the user has answered
    65 questions or when the time runs out.

    Returns:
        dict: A dictionary containing the following keys:
            - date (str): The date and time when the quiz was completed.
            - correct (int): The number of correct answers.
            - total (int): The total number of questions.
            - score (float): The percentage score.
            - status (str): "Pass" if the score is 70% or higher, otherwise "Fail".

    Raises:
        None

    Notes:
        - The quiz data is expected to be a list of dictionaries, where each dictionary represents a question
          with the following keys:
            - 'question' (str): The question text.
            - 'choices' (dict): A dictionary of choices where keys are choice labels (e.g., 'A', 'B') and values are the choice texts.
            - 'correct_answers' (list): A list of correct answer labels.
        - The function uses the curses library to handle terminal input and output.
        - The function assumes that the quiz data is available in the global scope as `quiz_data`.
    """
    correct = 0
    total = len(quiz_data)
    start_time = time.time()
    duration = 90 * 60  # 90 minutes
    screen = curses.initscr()

    # Shuffle the quiz data and select a random sample of up to 65 questions
    quiz_data_randomized = random.sample(quiz_data, min(65, len(quiz_data)))

    try:
        for question in quiz_data_randomized:  # Now using the randomized list of questions
            remaining_time = duration - (time.time() - start_time)
            if remaining_time <= 0:
                print("Time is up!")
                break

            screen.clear()
            screen.addstr(f"Time Remaining: {int(remaining_time // 60)}:{int(remaining_time % 60):02d}\n")
            screen.addstr(question['question'] + '\n')
            for key, value in question['choices'].items():
                screen.addstr(f"{key}: {value}\n")
            screen.addstr("E: Exit Quiz\n")
            screen.addstr("Your Answer: ")
            screen.refresh()
            answer = screen.getstr().decode("utf-8").strip().upper()
            if answer == "E":
                return {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "correct": correct,
                    "total": total,
                    "score": (correct / total) * 100,
                    "status": "Exited",
                }

            # Check if the answer is correct and show the correct answer
            if sorted(answer.split(", ")) == sorted(question['correct_answers']):
                correct += 1
                screen.addstr("Correct!\n")
            else:
                screen.addstr(f"Incorrect. The correct answer is: {', '.join(question['correct_answers'])}\n")
            
            screen.refresh()
            time.sleep(2)  # Pause for 2 seconds before moving to the next question

        # Calculate the score and return the result
        score = (correct / total) * 100
        status = "Pass" if score >= 70 else "Fail"
        return {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "correct": correct,
            "total": total,
            "score": score,
            "status": status,
        }
    finally:
        curses.endwin()

# Assuming the main function or quiz execution point below
if __name__ == "__main__":
    result = start_quiz()
    print(result)
