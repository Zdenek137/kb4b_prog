#import matplotlib.pyplot as plt
import csv
import random


#========================global constants=======================
path = r"my_programs/millionare/questions.csv"


easy_questions = []
medium_questions = []
hard_questions = []

general_knowledge_questions = []
entertainment_books_questions = []
entertainment_film_questions = []
entertainment_music_questions = []
entertainment_videogames_questions = []
science_nature_questions = []
science_computers_questions = []
geography_questions = []
history_questions = []


score = 0
lost = False

#====================Fill Lists====================================

with open(path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for line in reader:
        #difficulty
        if(line["difficulty"] == "easy"):
            easy_questions.append(line["id"])
        elif(line["difficulty"] == "medium"):
            medium_questions.append(line["id"])
        elif(line["difficulty"] == "hard"):
            hard_questions.append(line["id"])

        #category
        if(line["category"] == "General Knowledge"):
            general_knowledge_questions.append(line["id"])
        elif(line["category"] == "Entertainment: Books"):
            entertainment_books_questions.append(line["id"])
        elif(line["category"] == "Entertainment: Film"):
            entertainment_film_questions.append(line["id"])
        elif(line["category"] == "Entertainment: Music"):
            entertainment_music_questions.append(line["id"])
        elif(line["category"] == "Entertainment: Video Games"):
            entertainment_videogames_questions.append(line["id"])
        elif(line["category"] == "Science & Nature"):
            science_nature_questions.append(line["id"])
        elif(line["category"] == "Science: Computers"):
            science_computers_questions.append(line["id"])
        elif(line["category"] == "Geography"):
            geography_questions.append(line["id"])
        elif(line["category"] == "History"):
            history_questions.append(line["id"])

#====================Functions================================


#def show_question_count_graph():
    #plt.bar(["easy", "medium", "hard"], [len(easy_questions),len(medium_questions), len(hard_questions)],  color="blue")
    #plt.title("QUESTIONS")
    #plt.xlabel("type")
    #plt.ylabel("n")
    #plt.show()


def resolve_question(diff = "easy"): 
    #this function chooses a random question and checks input
    #player input must be TRUE or FALSE, in CAPS
    
    i = random.choice(easy_questions) if diff == "easy" else random.choice(medium_questions) if diff == "medium" else random.choice(hard_questions)

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for line in reader:
            if(i == line["id"]):
                print(line["question"])
                player_input = input(": ")

                if(str(line["correct_answer"]) == player_input):
                    print("correct")
                else:
                    print("wrong")
                    lost = True
                    exit
                break


#=====================Game Loop=================================



#show_question_count_graph()

#easy questions
for i in range(5):
    resolve_question("easy")
for i in range(5):
    resolve_question("medium")
for i in range(5):
    resolve_question("hard")

