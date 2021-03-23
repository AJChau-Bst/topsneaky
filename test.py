#import tbapy
#import numpy
import matplotlib.pyplot as plt
#import pandas
#import statsmodels
#import seaborn
#import plotly
# I forgot scikit learn
import random

print("fuck")
#ohno = input("How's ya fucking day? ")

#print (ohno)
#if(ohno=="bad"):
#    

print ("welcome to nim, you nerd.")


berries = random.randint(15,30)
pile = []
def display(berries):
    pile = []
    counter = 0
    while counter < berries:
        pile.append("O")
        counter += 1
    print(pile)
    print(berries)
    return(pile)

playerturn = 1

def turnover(playerturn,berries,pile): 
    if playerturn==1:
        print("Player 1's turn!")
    else:
        print("Player 2's turn!")

    reduction = input("How many berries will you take? (1, 2, or 3?) ")
    
    if reduction != '1' and reduction != '2' and reduction != '3':
        print ("Invalid input, try again loser")
        turnover(playerturn,berries,pile)
        
    
    berries = berries - int(reduction)
    
    if berries == 0:
        print("Player " + str(playerturn) + " won!")
        print("ha. sucker")
        print("NERDDDDD")
        quit()
    elif berries < 0:
        berries = berries + int(reduction)
        turnover(playerturn,berries,pile)

    display(berries)

    if playerturn==1:
        playerturn = 2
    else:
        playerturn = 1
    turnover(playerturn,berries,pile)

display(berries)
turnover(playerturn,berries,pile)

    