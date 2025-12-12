import matplotlib.pyplot as plt
import csv
import random

path = r"my_programs\millionare\millionare_questions.csv"


question_difficulties = [
    ["easy", 0],
    ["medium", 0],
    ["hard", 0]
]

question_categories = [
    ["General Knowledge", 0],
    ["Entertainment: Books", 0],
    ["Entertainment: Film", 0],
    ["Entertainment: Music", 0],
    ["Entertainment: Video Games", 0],
    ["Science: Nature", 0],
    ["Science: Computers", 0],
    ["Geography", 0],
    ["History", 0]
]


with open(path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for line in reader:
        if(line["difficulty"] == "easy"):
            question_difficulties[0][1] += 1
        elif(line["difficulty"] == "medium"):
            question_difficulties[1][1] += 1
        else:
            question_difficulties[2][1] += 1
#===============================================================


def show_question_count_graph():
    plt.bar([question_difficulties[0][0], question_difficulties[1][0], question_difficulties[2][0]], 
    [question_difficulties[0][1], question_difficulties[1][1], question_difficulties[2][1]], color="blue")
    plt.title("QUESTIONS")
    plt.xlabel("type")
    plt.ylabel("n")
    plt.show()


def resolve_question(diff = "easy"):
    rand_int = random.randint(0, 261)

    i = 0


    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for line in reader:
            if(i == rand_int):
                print(line["question"])
                player_input = input(": ")

                if(str(line["correct_answer"]) == player_input):
                    print("correct answer")
                else:
                    print("false answer")
                
                break
            i += 1


#===============================================================
#game loop


show_question_count_graph()
#easy questions
for i in range(5):
    resolve_question()

