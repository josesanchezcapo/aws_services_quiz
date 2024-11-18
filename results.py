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

import json
from datetime import datetime


RESULTS_FILE = "results_data.json"


def save_result(result):
    try:
        with open(RESULTS_FILE, "r") as file:
            results = json.load(file)
    except FileNotFoundError:
        results = []

    results.append(result)
    with open(RESULTS_FILE, "w") as file:
        json.dump(results[-10:], file, indent=4)


def view_past_results():
    try:
        with open(RESULTS_FILE, "r") as file:
            results = json.load(file)
    except FileNotFoundError:
        print("No past results found.")
        return

    print("Past Results:")
    print("=============")
    for result in results:
        print(f"Date: {result['date']}, Score: {result['score']:.2f}%, Status: {result['status']}")
