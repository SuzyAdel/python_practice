#bro code practice 2 : quiz game 
#--------------------------------------------
def score(correct_guesses,guesses):
    print("results!!")
    print("correct answeres:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ") #dictionary
     
    print("your guesses:", end=" ")
    for i in guesses:
        print(i, end=" ") # list 
    
    res=int(correct_guesses/len(questions))*100
    print("your result is",res,"%") #or + str(res) +

#--------------------------------------------
def play_again():
    response=input("Do you want to play again? Y/N").upper
    if response== "Y":
        return True 
    else:
        return False 


def new_game():
    guesses=[]
    correct_guesses=0
    question_number=1

    for key in questions:
        print("--------------------------------------------")
        print(key)

    for i in options[question_number-1]:
        # lists starts from 0 thus -1
        print(i)

    guess=input("enter {A,B,C OR D}: ").upper()
    guesses.append(guess)

    check(questions.get(key),guess)
    correct_guesses += check
    question_number +=1 

    s=score(correct_guesses,guesses)
    p=play_again()

#--------------------------------------------
def check(answer,guess):
    if answer == guess:
        print('correct')
        return 1
    else:
        print('incorrect')
        return 0

    

#--------------------------------------------
questions={
    "what is the largest animal in the world?": "A",
    "what is the most popular game of all time?":"B",
    "what is the most relaxing colour?":"C",
    "what is the ritchest company ?":"A"
    } #dictonary
options=[
    ["A.blue whale B.elephant c.giraffe d.gorrilas"],
    ["A.super mario B.mincraft C.subway surface D.pac-man"],
    ["A.white B.light green C.navy blue D.grey"],
    ["A.apple B.microsoft C.google D.amazon"]
      ]#2d list

new_game()

while play_again:
    #returns true or false 
    new_game()
    
print('BYEE')