
# AWS Quiz Application

## Overview
This repository contains a Python-based quiz application designed to help users test their knowledge of AWS concepts and services. The quiz features a dynamic countdown timer, a modular design, persistent result storage, and the ability to view past results. It is an ideal tool for practicing AWS knowledge and preparing for certifications or interviews.

## Features
- **Menu System:** Easy navigation with options to start the quiz, view past results, or exit.
- **Multiple-choice questions:** Test your knowledge of various AWS services, with some questions requiring multiple correct answers.
- **Dynamic Countdown Timer:** Track your remaining time with a 90-minute timer during the quiz session.
- **Scoring and Results:** Your score is automatically calculated based on the number of correct answers, and the application determines whether you pass (70% or higher).
- **Past Results:** View your last 10 quiz attempts, including score percentages and pass/fail status.
- **Modular Design:** The application is split into separate files for easier maintenance and debugging.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aws-quiz-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd aws-quiz-app
   ```
3. Ensure you have Python installed (preferably Python 3.6 or higher).
4. Run the `main.py` file to start the application:
   ```bash
   python main.py
   ```
5. Follow the on-screen instructions:
   - Select the **Start Quiz** option to begin.
   - View past quiz results with the **View Past Results** option.
   - Exit the application by choosing the **Exit** option.

## File Structure
The project contains the following files:
- **`menu.py`**: Handles the menu display and user input for navigation.
- **`quiz.py`**: Manages the quiz logic, timer, question display, and result calculation.
- **`results.py`**: Manages result storage and displays past results.
- **`quiz_data.py`**: Stores the quiz questions and correct answers.
- **`main.py`**: The entry point of the application that ties everything together.

## Disclaimer
The information provided in this quiz is based on publicly available documentation from the official AWS website (https://aws.amazon.com).  
This quiz is offered "as is" for educational purposes only, with no guarantees of accuracy, completeness, or suitability for any purpose.  
For the most accurate and up-to-date information, please refer to the official AWS documentation.

## Feedback
If you encounter any errors, have suggestions for improvements, or would like to modify this quiz to better fit your needs, please feel free to provide feedback. Your input is greatly appreciated and helps improve the quality of this resource.

## Author
**Name:** Jose Sanchez-Capo  
**Email:** [josesanchezcapo@gmail.com](mailto:josesanchezcapo@gmail.com)
