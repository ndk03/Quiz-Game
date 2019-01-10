import random
"""
Quiz application that randomly generates 3 questions each time
"""
filename = "QuizQuestion.txt"
file  = open(filename, "r")
question = []
answers = []
que = ""

for line in file:
    if line.strip() != '|':
        que += line
    else:
        question.append(que)
        que = ""

with open('answers.csv') as csvfile:

    for row in csvfile:
        answers.extend(row.split(','))


count = 1
tempQuestion = question.copy()
tempAnswer = answers.copy()
score = 0

while(count<=3):
    select = random.randint(0,len(tempQuestion)-1)
    print(f"question{count}")
    print(tempQuestion[select])
    ans = input("enter your option\n")
    if(ans.lower() == answers[select]):
        print("Correct\n")
        score += 10
    else:
        print("Wrong")

    tempQuestion.pop(select)
    tempAnswer.pop(select)
    count += 1
print("Score ",score)
