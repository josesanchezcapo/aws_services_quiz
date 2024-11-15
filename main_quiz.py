# main_quiz.py - Main logic for the quiz

import random
from quiz_data import quiz_data

def run_quiz():
    correct_answers = 0
    total_questions = len(quiz_data)
    selected_questions = random.sample(quiz_data, total_questions)

    for idx, item in enumerate(selected_questions, 1):
        print(f"\nQuestion {idx}: {item['question']}")
        for choice in item['choices']:
            print(choice)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == item['answer']:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was {item['answer']}.")

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

