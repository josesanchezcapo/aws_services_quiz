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
from datetime import datetime
from quiz_data import quiz_data


def start_quiz():
    correct = 0
    total = len(quiz_data)
    start_time = time.time()
    duration = 90 * 60  # 90 minutes
    screen = curses.initscr()

    try:
        for question in quiz_data[:65]:  # Limit to 65 questions
            remaining_time = duration - (time.time() - start_time)
            if remaining_time <= 0:
                print("Time is up!")
                break

            screen.clear()
            screen.addstr(f"Time Remaining: {int(remaining_time // 60)}:{int(remaining_time % 60):02d}\n")
            screen.addstr(question['question'] + '\n')
            for key, value in question['choices'].items():
                screen.addstr(f"{key}: {value}\n")

            screen.addstr("Your Answer: ")
            screen.refresh()
            answer = screen.getstr().decode("utf-8").strip().upper()
            if sorted(answer.split(", ")) == sorted(question['correct_answers']):
                correct += 1

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
