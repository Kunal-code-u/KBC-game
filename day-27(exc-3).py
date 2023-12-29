# Create a program capable of displaying questions to user like KBC
# Use list data type to store questions and their correct answers
# Display the final amount the person is taking home after playing the game

# importing random module to shuffle the questions
# import random
# prize_money = 0

# questions = [{
#     "question": "What is the capital of India?",
#     "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4.Chennai"],
#     "answer": 1
# },{
#     "question": "Which planet is know as the Red Planet?",
#     "options": ["1. Jupiter", "2. Venus", "3. Mars", "4. Saturn"],
#     "answer": 3
# },{
#     "question": "Who painted the Mona Lisa?",
#     "options": ["1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet"],
#     "answer": 3 
# }]

# random.shuffle(questions)

# for question in questions:
#     print(question["question"])
#     for option in question["options"]:
#         print(option)

#     user_answer = int(input("Enter your answer(option number): "))        

#     if user_answer == question["answer"]:
#         print("Correct answer!")
#         prize_money += 1000
#     else:
#         print("Wrong answer!")
#         break

# print("Prize Money:", prize_money)


questions = [  # Created a list to store questions and answers
    ["Which language was used to make fb?", "Python", # 0 th
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python", # 1 st 
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python", # 2 nd
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
    
    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],

    ["Which language was used to make fb?", "Python",
     "French", "JavaScript", "Php", "None", 4],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]  # This is prize money
money =  0 # Initially prize money is set to 0

for i in range(0, len(questions)):
    question = questions[i] # for i = 0 question 1 in list
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}      b. {question[2]} ")
    print(f"c. {question[3]}      d. {question[4]} ")
    reply = int(input("Enter your answer(1-4) or 0 to quit: "))
    if(reply == 0):
        money = levels[i - 1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000    
    else:
        print("Wrong answer!")
        break
    
print(f"Your take home money is {money}")