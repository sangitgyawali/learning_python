# Python quiz game

questions = ("How many letters are in the alphabet?",
             "What is the capital of France?", 
             "What is the largest planet in our solar system?",
             "What is the boiling point of water in degrees Celsius?",
             "What is the chemical symbol for gold?")


options = (["A.116", "B.26", "C.30", "D.24"],
           ["A.Madrid", "B.Paris", "C.Berlin", "D.Rome"],
           ["A.Earth", "B.Mars", "C.Jupiter", "D.Saturn"],
           ["A.90", "B.100", "C.80", "D.120"],
           ["A.Fe", "B.Cu", "C.Au", "D.Ag"])

answers = ("B",  
           "B",  
           "C",  
           "B",  
           "C"  
)
score = 0

for question_num, question in enumerate(questions):
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter A, B, C, or D: ").upper()
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer was", answers[question_num])
print(f"Your score is {score}/{len(questions)}")