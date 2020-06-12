from tkinter import *
from PIL import ImageTk, Image
import tkinter
import time
import random
import math
import operator

def main():


    name1=str(input('Player 1 name: '))
    name2=str(input('Player 2 name: '))
    end_goal=int(input('What score do you want to play to for a win?'))
    highest_range1=int(input('What is the maximum number you want to work with with ' +name1 +"?"))
    highest_range2=int(input('What is the maximum number you want to work with with ' + name2 + "?"))
    difficulty1=int(input(name1+ ' press 1 for addition and subtraction, select 2 to add multiplication, or 3 if you want addition, subtraction, multiplication, and division:'))
    difficulty2=int(input(name2 + ' press 1 for addition and subtraction, select 2 to add multiplication or 3 if you want addition, subtraction, multiplication, and division:'))
    math_problem(highest_range1, highest_range2, difficulty1, difficulty2, name1, name2, end_goal)
    input('Press Enter to begin...')


def math_problem(highest_range1, highest_range2, difficulty1, difficulty2, name1, name2, end_goal):
    p1_counter=0
    p2_counter=0
    p1_timer=0
    p2_timer=0
    turn_counter=0
    while p1_counter<end_goal or p2_counter<end_goal:
        math = {"+": operator.add, "-": operator.sub,"*": operator.mul, '/': operator.truediv}
        if difficulty1==1:
            op = random.choice(["+", "-"])
        elif difficulty1==2:
            op=random.choice(["+", "-", "*"])
        else:op = random.choice(["+", "-", "*", "/"])

        #player1 random numbers

        number_1 = int(random.randint(1, highest_range1))
        number_2 = int(random.randint(1, highest_range1))
        #player2 random numbers
        number_3 = random.randint(1, highest_range2)
        number_4 = random.randint(1, highest_range2)
        #player1
        start_time=time.time()
        operation=op
        if operation=="/":
            number_1=number_2*int(random.randint(2,5))
            answer = math[op](number_1, number_2)
            user_input=int(input(name1+" what is "+str(number_1)+ operation+ str(number_2)+"? "))
            if user_input==answer:
                print('Correct!')
                p1_counter+=1
            else:print('Incorrect!')
        elif operation=="-":
            if number_2>=number_1:
                variable_1=number_1
                number_1=number_2
                number_2=variable_1
                answer = math[op](number_1, number_2)
                user_input = int(input(name1 + " what is " + str(number_1) + op + str(number_2) + "? "))
                if answer == user_input:
                    print('Correct!')
                    p1_counter += 1
                else:
                    print('Incorrect!')
        else:
            answer = math[op](number_1, number_2)
            user_input = int(input(name1 + " what is " + str(number_1) + op + str(number_2) + "? "))
            if answer==user_input:
                print('Correct!')
                p1_counter+=1
            else:print("Incorrect!")
        time_spent=time.time()-start_time
        p1_timer+=time_spent


        #player2
        if difficulty2 == 1:
            op2 = random.choice(["+", "-"])
        elif difficulty2 == 2:
            op2 = random.choice(["+", "-", "*"])
        else:
            op2 = random.choice(["+", "-", "*", "/"])
        start_time2=time.time()
        operation2=op2
        if operation2=="/":
            number_3=number_4*int(random.randint(2,5))
            answer = math[op2](number_3, number_4)
            user_input = int(input(name2+" what is " + str(number_3) + op2 + str(number_4) + "? "))
            if answer == user_input:
                print('Correct!')
                p2_counter+=1
            else:print('Incorrect!')
        elif operation2=="-":
            if number_4>=number_3:
                variable_2=number_3
                number_3=number_4
                number_4=variable_2
                answer = math[op2](number_3, number_4)
                user_input = int(input(name2 + " what is " + str(number_3) + op2 + str(number_4) + "? "))
                if answer == user_input:
                    print('Correct!')
                    p2_counter += 1
                else:
                    print('Incorrect!')
        else:
            answer = math[op2](number_3, number_4)
            user_input = int(input(name2 + " what is " + str(number_3) + op2 + str(number_4) + "? "))
            if answer == user_input:
                print('Correct!')
                p2_counter += 1
            else:
                print('Incorrect!')

        time_spent = time.time() - start_time2
        p2_timer+=time_spent
    print('Score is ' + name1 +' '+ str(p1_counter) + ' and ' + name2 +' '+ str(p2_counter) + ".")
    if p1_counter==p2_counter:
        print('Weve have a tie!!! Whomever had the least time will win!')
        print(name1+' ' +str(p1_timer)+'seconds!')
        print(name2+' '+str(p2_timer)+ 'seconds!')
        if p1_timer<p2_timer:
            print(name1+'Wins!!!')
        else:print(name2+'Wins!!!')
    else:
        if p1_counter>p2_counter:
            print(name1+ ' wins!')
        else:print(name2+ ' wins!')
    print('')
    end_game_options=input("Restart game with same settings?(Yes or No):")
    if end_game_options=="Yes":math_problem(highest_range1, highest_range2, difficulty1, difficulty2, name1, name2, end_goal)
    else:("Restart game yourself. I'm too lazy to add all that code.")










# creates an easy math problem








if __name__ == '__main__':
    main()