# AWS Quiz Program

# Quiz questions and answers
quiz_data = [
    {"question": "What is Amazon EC2 used for?", "answer": "Scalable virtual servers for compute capacity in the cloud."},
    {"question": "What does Amazon S3 provide?", "answer": "Object storage built to store and retrieve any amount of data from anywhere."},
    {"question": "What is Amazon RDS?", "answer": "Managed relational database service for databases like MySQL, PostgreSQL, and Oracle."},
    {"question": "What is AWS Lambda used for?", "answer": "Run code without provisioning or managing servers. Pay only for the compute time used."},
    {"question": "What is Amazon DynamoDB?", "answer": "Fast and flexible NoSQL database service for single-digit millisecond performance."},
    {"question": "What does Amazon VPC enable?", "answer": "Provision a logically isolated network in the AWS Cloud."},
    {"question": "What is Amazon CloudFront?", "answer": "Content Delivery Network (CDN) for delivering data, videos, applications, and APIs securely."},
    {"question": "What is AWS IAM?", "answer": "Securely manage access to AWS services and resources."},
    {"question": "What does Amazon SNS do?", "answer": "Pub/sub messaging for microservices, distributed systems, and serverless applications."},
    {"question": "What is Amazon SQS?", "answer": "Message queuing service to decouple and scale microservices, distributed systems, and serverless applications."}
]

# Initialize counters
correct_answers = 0
incorrect_answers = 0

# Quiz loop
print("Welcome to the AWS Quiz!")
print("Answer each question based on the provided AWS descriptions.")
print("----------------------------------------------------------")

for idx, item in enumerate(quiz_data, start=1):
    print(f"Question {idx}: {item['question']}")
    user_answer = input("Your answer: ").strip()
    
    if user_answer.lower() == item['answer'].lower():
        print("Correct!\n")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is: {item['answer']}\n")
        incorrect_answers += 1

# Calculate the percentage
total_questions = len(quiz_data)
percentage = (correct_answers / total_questions) * 100
result = "Passed" if percentage >= 70 else "Failed"

# Summary
print("----------------------------------------------------------")
print(f"Quiz Summary:")
print(f"Correct Answers: {correct_answers}")
print(f"Incorrect Answers: {incorrect_answers}")
print(f"Score: {percentage:.2f}%")
print(f"Result: {result}")
print("----------------------------------------------------------")
