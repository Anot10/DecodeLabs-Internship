
score = 0

print("Welcome to the Quiz Game!")
print("Answer the following 3 questions.\n")

# Question 1
answer = input("1. What is the national animal of India? ")

if answer.lower() == "tiger":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is Tiger.")

# Question 2
answer = input("\n2. How many days are there in a week? ")

if answer == "7":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is 7.")

# Question 3
answer = input("\n3. What is the capital of India? ")

if answer.lower() == "new delhi":
    print("Correct answer!")
    score = score + 1
else:
    print("Wrong answer! The correct answer is New Delhi.")

# Final Score
print("\nQuiz Completed!")
print("Your final score is:", score, "/ 3")
