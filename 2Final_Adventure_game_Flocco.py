#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 03:45:53 2018



@author: ludovicaflocco
"""
"""
Docstring
The Hangover is a 3 stage adventure text game. 
You will be called to play 3 rounds:
    Round 1: you have to decide what to drink and in what amount 
    Round 2: you have to deal with an unexpected situation 
    Round 3: you have to take a wild guess
    
Enjoy your game and drink responsably 
"""


import pandas as pd
from sys import exit
import random

def game_start():
    print("""
          You are a 23 years-old graduate student who is tormented between the burden of your responsibilities and the wild desire to party. 
          It’s Halloween night and you’ve been invited to a friend place for an ultimate night of fun, pleasure and amusement. It’s the party of the year. One rule only: Bottoms up.
          However, tomorrow 1st of November, your Data Science professor has scheduled a class presentation for you to deliver, worth more than half of your grade. 
          Your goal tonight is to maximize your fun without compromising your class performance tomorrow. Bear in mind: no one likes a party pooper. 
          Any similarity to real life events or persons, living or dead, is purely coincidental. Or maybe not.
          """)
    input("Press enter to continue")
    part_1()

def part_1():
    print("""
          Are you ready?
      1. Yes
      2. No
      """)
    
    ready = input("> ")
    if '1' in ready or 'Yes' in ready or 'yes' in ready:
        print("""
      ___           ___           ___           ___                    ___           ___     
     /\__\         /\  \         /\  \         /\__\                  /\  \         /\  \    
    /:/ _/_       /::\  \       |::\  \       /:/ _/_                /::\  \        \:\  \   
   /:/ /\  \     /:/\:\  \      |:|:\  \     /:/ /\__\              /:/\:\  \        \:\  \  
  /:/ /::\  \   /:/ /::\  \   __|:|\:\  \   /:/ /:/ _/_            /:/  \:\  \   _____\:\  \ 
 /:/__\/\:\__\ /:/_/:/\:\__\ /::::|_\:\__\ /:/_/:/ /\__\          /:/__/ \:\__\ /::::::::\__\
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \:\/:/ /:/  /          \:\  \ /:/  / \:\~~\~~\/__/
  \:\  /:/  /   \::/__/       \:\  \        \::/_/:/  /            \:\  /:/  /   \:\  \      
   \:\/:/  /     \:\  \        \:\  \        \:\/:/  /              \:\/:/  /     \:\  \     
    \::/  /       \:\__\        \:\__\        \::/  /                \::/  /       \:\__\    
     \/__/         \/__/         \/__/         \/__/                  \/__/         \/__/    
""")
        input("Press enter to continue")
        part_2()        

    elif '2' in ready or 'No' in ready or 'no' in ready or 'NO' in ready:
        print("Don't be a Party Pooper!\n")
        print("""Did you change your mind? 
              1. Yes
              2. No
              """)
        answer_1=input('> ')

        if answer_1=='1' or"yes"or answer_1=="Yes" or answer_1=="YES" or answer_1=="y" or answer_1=="Y":
            print("""
      ___           ___           ___           ___                    ___           ___     
     /\__\         /\  \         /\  \         /\__\                  /\  \         /\  \    
    /:/ _/_       /::\  \       |::\  \       /:/ _/_                /::\  \        \:\  \   
   /:/ /\  \     /:/\:\  \      |:|:\  \     /:/ /\__\              /:/\:\  \        \:\  \  
  /:/ /::\  \   /:/ /::\  \   __|:|\:\  \   /:/ /:/ _/_            /:/  \:\  \   _____\:\  \ 
 /:/__\/\:\__\ /:/_/:/\:\__\ /::::|_\:\__\ /:/_/:/ /\__\          /:/__/ \:\__\ /::::::::\__\
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\  \/__/ \:\/:/ /:/  /          \:\  \ /:/  / \:\~~\~~\/__/
  \:\  /:/  /   \::/__/       \:\  \        \::/_/:/  /            \:\  /:/  /   \:\  \      
   \:\/:/  /     \:\  \        \:\  \        \:\/:/  /              \:\/:/  /     \:\  \     
    \::/  /       \:\__\        \:\__\        \::/  /                \::/  /       \:\__\    
     \/__/         \/__/         \/__/         \/__/                  \/__/         \/__/    
""")
            input("Press enter to continue")
            part_2()
            
        elif answer_1=="no" or 'No' or 'NO' or 'n' or '2':
            print("You are not being very supportive here.")
            input("Press enter to continue")
            game_start()
        
        else:
            print("invalid entry")
            input("Press enter to continue")
            part_1()
       
    else:
        print("invalid entry")
        input("Press enter to continue")
        part_1()


def part_2():
    print("""
          Your first task is to decide what to drink and in what amount. 
          From personal experience you know how your body reacts with different alcoholic beverages. Use the following knowledge to make a conscious choice. 

        Remember that, in order to succeed as a Party Shaker, you want to avoid both too little and too much drinking. Pick the right combination to enjoy your party out of beer, wine and cocktails.
        """)
    input("<Press enter to continue>\n")
    
    alcohol = ['Beer', 'Wine','Cocktail']
    per_mille = [.01, .023, .03]
    dictionary = {'BEVERAGE': alcohol, 'Blood Alcohol Content %': per_mille}
    alcohol_table = pd.DataFrame(dictionary)
    alcohol_table.index =["1", "2", "3"]
    
    print(alcohol_table)
    input("<Press enter to continue>\n")

    
    cups_of_beer = input("How many beers would you like to drink? \n>")
    if cups_of_beer.isdigit():
        print("")
    else:
        print("Invalid entry. Please enter a number")
        part_2()
    
    glasses_of_wine = input("How many wine glasses would you like to start with? \n> ")
    if glasses_of_wine.isdigit():
        print("")
    else:
        print("Invalid entry. Please enter a number")
        part_2()
    
    number_of_cocktails = input("How many cocktails would you like to have? \n> ")
    if number_of_cocktails.isdigit():
        print("")
    else:
        print("Invalid entry. Please enter a number")
        part_2()
        
    x = int(cups_of_beer) *.01 
    y = int(glasses_of_wine) * .023 
    z = int(number_of_cocktails) * .03
    
    if x + y + z <= .05 :
        fail()
    
    elif x+ y + z >.05 and x+ y +z <.09:
        print("Everybody is a little tipsier than you, you might want to catch up")    
        input("<Press enter to continue>\n")  
        part_3()
    
    elif x+ y +z >=.09 and x+ y + z<=0.15:
        print("""
          Well done! The sky tonigh is your only limit. 
          """)
        input("<Press enter to continue>\n")
        part_3()
    
    elif x + y + z > 0.15:
        too_much()
            
    else:
        print('invalid entry')
        part_2()

def fail():
    print("""
          You were drinking way too little to keep up with the rest of the crowd.
          Now the entire school thinks you're a moron. You're reputation is ruined. 
          Let's pray that you will at least get a High Pass tomorrow '\#LOSER
          """)
    input("<Press enter to continue>\n") 
    print("Let's try again")
    input("<Press enter to continue>\n")
    part_2()
    
def too_much():
    print("""
          You got way too excited way too soon.
          As a result you passed out on your friend couch like a little girl at the very beginning of the night.
          Who knows if you will make it to class tomorrow.
          """)
    input("<Press enter to continue>\n") 
    print("Let's try again")
    input("<Press enter to continue>\n")
    part_2()

    
def part_3():
    print("""
          Halfway through the night your Ex shows up at the party looking pretty damn steamy. 
          As if being there wasn’t enough to ruin your fun, he/she decides to come up and talk to you. As you see him/her approaching, you start panicking. You really don’t want to talk to him/her.
          Quick, what do you do to avoid this awkward conversation?
          1)	No matter the identity, you grab the closest person next to you and passionately start making out with them.
          2)	To create a diversion, you challenge your friends to an epic dance battle. No discounts: chicken dance, moonwalk and twerking all included.
          3)	Out of options, you make a scene and through your drink at your ex's face because let’s face it she/he deserves it.
    
          Careful:  each action will be directly correlated to a specific consumption of alcohol to deal with its embarrassing consequences
          """)
    choice = input(">  \n")

    if "1" in choice or "making out" in choice or "grab" in choice:
        print("\n\t You made out with your cousin, that's a little disgusting. You need 3 shots to forget.\n")
        input("<Press enter to continue>\n")
        part_4()
     
    
    elif "2" in choice or "diversion" in choice or "dance battle" in choice:
        print(f"""\n\t You've got moves! Everybody loved your performance and you even sobered up by dancing. To reward yourself you get yourself a refreshing Mojito.\n""")
        input("<Press enter to continue>\n")
        part_4()
        
        
    elif "3" in choice or "make a scene" in choice or "threaten" in choice or "ex face" in choice:
       fail_1()
       
    
    else:
        print("""\n This command is not working here. Please type "1", "2", or "3". """)
        input("<Press enter to continue>\n")
        part_3()
    
def fail_1():
    print("You get a standing ovation by all your friends however the hosts ask both you and your ex to leave the party. Game Over!")
    print("""Would you like to play again? 
          1. Yes
          2. No
          """)
    reply = input("> ")
    reply = reply.lower()
    
    if reply == 'yes' or '1':
        game_start()
        
    elif reply== 'no' or '2':
        print("Thanks for playing, Cheers!")
        exit(0) 
        
    else:
        print("Thanks for playing, Cheers!")
        exit(0)

def fine():
    print("""
          You are forced to down another drink. 
          That makes you blackout completely 
          The next morning you wake up at noon in an apartment that is not yours with no phone, no shoes and no dignity.
          Being irresponsible compromise your grade, learn from your mistakes.
          """)
    print("""Would you like to play again? 
          1. Yes
          2. No
          """)
    replay = input("> ")
    replay = replay.lower()
    
    if 'yes' in replay or '1' in replay:
        game_start()
        
    elif 'no'in replay or '2' in replay:
        print("Thanks for playing, Cheers!")
        exit(0)
    else:
        print("Thanks for playing, Cheers!")
        exit(0) 
        

        
        
def part_4():
    print("""
          At this point of the night you reached your maximum capacity. You shouldn’t drink anymore if you’d like to make it to class tomorrow. 
          However, knowing how competitive you are, your best friend, Chase, comes to you with the ultimate drinking challenge. Guess the number of fingers he is holding below his back or down an entire drink. You’re aware that you should call it a night, but mama didn’t raise a quitter. However, in order to increase your chances of winning you demand to have 3 guesses. Your friend accepts and the game is on.
          """)
    input("<Press enter to continue>\n")
    print("""
          Remember you can only guess 3 times and if you lose your academic distinction is on the line.
          """)
    number=random.randint(1,10)
    
    guesses = 3
    
    while guesses > 0:
        print("\nHow many fingers is Chase hiding behind his back? 1-10")
        choice = input("> ")
        if choice.isdigit() and int(choice) in range(1,11):
            if choice == number:
                print("\nYou master the art of wild guessing!")
                input("<Press enter to continue>\n")
                print("""
                  You officially completed the night the best way possible. 
                  Good luck on yourpresentation tomorrow, you'll nail it!
                  """)
                winning()
            elif choice != number:
                print("\nThat's incorrect, please guess again.")
                guesses -= 1
                if guesses == 0:
                    print(f"\nYou are out of guesses. The number was {number}.")
                    fine()
#            elif choice != number:
#                print("How many fingers do you have? You can only guess up to 10!")
#                guesses -= 1
#                if guesses == 0:
#                        print(f"\nYou are out of guesses. The number was {number}.")
#                        fine()
            else: 
                print("Something went wrong")
                part_4()
        else:
            print("Invalid entry. Please enter a number between 1 and 10")
            part_4()

       
            

def winning():
    print("""Would you like to play again? 
          1. Yes
          2. No
          """)
    reply = input("> ")
    reply = reply.lower()
    
    if 'yes' in reply or '1' in reply:
        game_start()
        
    elif 'no' in reply or '2' in reply:
        print("Thanks for playing, Cheers!")
        exit(0) 
        
    else:
        print("Thanks for playing, Cheers!")
        exit(0) 
        
    
###########################
        
game_start()


