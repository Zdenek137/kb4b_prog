#import matplotlib.pyplot as plt
import csv
import random
import sys
import os

#========================global variable and constants=======================
path = r"my_programs/millionare/questions.csv"
users_path = r"my_programs/millionare/users.csv"

users_data = dict()

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
round = 1

signed_in_user_username = ""

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

#! Remove '#' to enable graph showing function
#def show_question_count_graph():
#    plt.bar(["easy", "medium", "hard"], [len(easy_questions),len(medium_questions), len(hard_questions)],  color="blue")
#    plt.title("QUESTIONS")
#    plt.xlabel("type")
#    plt.ylabel("amount")
#    plt.show()
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def resolve_question(diff = "easy"): 
    #this function chooses a random question and checks input
    #player input must be TRUE or FALSE, in CAPS

    #global [variable] is added to tell the function it is working with a global variable and not a local one
    global round
    global score
    global users_data

    i = random.choice(easy_questions) if diff == "easy" else random.choice(medium_questions) if diff == "medium" else random.choice(hard_questions)

    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for line in reader:
            if(i == line["id"]):
                print(line["question"])
                player_input = input("You answer > ")

                if(str(line["correct_answer"]) == player_input):
                    print("Correct")
                    round += 1
                    score += round ** 2 * 5
                else:
                    print("Wrong")
                    print("Score: ", score)
                    print("Highest score: ", [user_line["highest_score"] for user_line in users_data if user_line["username"] == signed_in_user_username][0])
                    print("Round: ", round)
                    
                    #update user highest_score in users.csv
                    for user_line in users_data:
                        if(user_line["username"] == signed_in_user_username):
                            if(int(user_line["highest_score"]) <= int(score)):
                                user_line["highest_score"] = str(score)
                            break
                    
                    with open(users_path, "w", encoding="utf-8", newline='') as file:
                        fieldnames = ["id", "username", "password", "highest_score"]
                        writer = csv.DictWriter(file, fieldnames = fieldnames)
                        writer.writeheader()
                        writer.writerows(users_data)

                    input("Press enter to exit")
                    sys.exit(1)
                    exit
                break


#=====================Game Loop=================================

#initial read to fill users_file_reader
with open(users_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    users_data = [row for row in reader]

#========Sign up / Sign in========

print("1 - sign up")
print("2 - sign in")


if(str(input("> ")) == "1"):
    with open(users_path, "a", encoding="utf-8") as file:
        file.write("0," + str(input("Username: ")) + "," + str(input("Password: ")) + ",0\n")
else:
    logging_in = True
    while(logging_in):
        clear_terminal()
        with open(users_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if(str(line["username"]) == str(input("Username: ")) and str(line["password"]) == str(input("Password: "))):
                    print("Welcome back ", line["username"])
                    signed_in_user_username = line["username"]
                    logging_in = False
                    break
                else:
                    print("Wrong username or password")
                    break
        input("")

#========Show graph / Play========
clear_terminal()
print("MENU")
print("1 - show graph")
print("2 - play")

if(str(input("> ")) == "1"):
    clear_terminal()
    #! remove '#' to enable graph showing function
    #show_question_count_graph()
    print()
else:
    clear_terminal()
    #easy questions
    for i in range(5):
        resolve_question("easy")
    #medium questions
    for i in range(5):
        resolve_question("medium")
    #hard questions
    for i in range(5):
        resolve_question("hard")
    print("Congratulations! You win!")
    print("Score: ", score)
    print("Highest score: ", [user_line["highest_score"] for user_line in users_data if user_line["username"] == signed_in_user_username][0])
    print("Round: ", round)

