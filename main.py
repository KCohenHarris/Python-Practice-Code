#A new quiz game will be created
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
#---------------------------------------
#The answer will be checked if right or wrong
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!!")
        return 1
    else:
        print("WRONG!!!")
        return 0

#---------------------------------------
#The score will be displayed
def display_score(correct_guesses, guesses):
    print("--------------------------------------")
    print("RESULTS")
    print("--------------------------------------")
    print("Answers: ", end=" ")

    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#---------------------------------------
#As if would like to play again
def play_again():


    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#---------------------------------------
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is attributed to which comedy group?: ": "C",
    "Is the Earth round?: " : "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What is Earth?"]]

new_game()

while play_again():
    new_game()

print("Thanks for Playing!!")