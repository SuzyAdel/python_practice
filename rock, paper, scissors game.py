#bro code practice 1: rock, paper, scissors game
import random 

play_again='yes'
score=0
while play_again=="yes":
    
    choices=['rock', 'paper','scissors']
    player=None
    computer= random.choice(choices) 

    while player not in choices:
        player= input("enter rock, paper or scissors: ").lower()

    def results(): #print the round results
        print('player : ', player)
        print('computer: ', computer)

    if player==computer:
        results()
        print("TIE")

    elif player=='rock':
        if computer=='paper':
            results()
            print('COMPUTER WINS')
            print('YOUR SCORE IS= ',score)
        else:
            #scissors
            results()
            print('YOU WIN')
            score+=1 
            print('YOUR SCORE IS= ',score)

    elif player=='paper':
        if computer=='scissors':
            results()
            print('COMPUTER WINS')
            print('YOUR SCORE IS= ',score)
        else:
            #rock
            results()
            print('YOU WIN')
            score+=1 
            print('YOUR SCORE IS= ',score)

    elif player=='scissors':
        if computer=='rock':
            results()
            print('COMPUTER WINS')
            print('YOUR SCORE IS= ',score)
        else:
            #paper
            results()
            print('YOU WIN')
            score+=1 
            print('YOUR SCORE IS= ',score)

    play_again= input('do you want to play again? (yes/no);' ).lower()

    if play_again!= 'yes':
        print("this round's score was= ", score)
        break
print('BYEE!!')
            


