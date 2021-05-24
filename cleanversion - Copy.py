#How to play!
#Nim is a game theory mathematical game. The player wins by being the last person to take berries from the pile, however both players are restricted to only taking 1, 2 or 3
# berries. Players take turns to take from the main pile until none are left. 

#The first prompt given to the user asks how many players will be playing. The main game-mode is one with 1 player and the user goes against the computer. However, the user can
#also select 0 players, allowing the computer to train against itself for a better algorithm or 2 players, where 2 people can enter in their desired number in the terminal. 
#This is meant to currently be played in a terminal, using the run command python3 cleanversion.py

#In addition, this program exports an image after every generation that shows the computer's progress in learning. This may be put into the same folder that this program
#is running in. 


#imported several libraries here
import numpy as np
import matplotlib.pyplot as plt
import csv
import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
import random

#this is code imported from Udacity U120 lesson on learning. It functions as a visual way for program testers to see what the computer is thinking
from class_vis import prettyPicture, output_image

#set of training data given to the computer at the start of the program
berryFeatures1 = np.array([[30,2], [27,3], [22,2], [21,1], [18,2], [17,1], [17,1], [14,2], [13,1], [10,2], [9,1], [7,3], [3,3], [2,1], [17,2], [17,3], [15,3], [15,1], [15,2], [15,3], [14,2], [14,1], [14,3]])
berryLabels1 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,2,2,1,1,2,2])
berryFeaturesCache1 = np.array([[32,5]])

berryFeatures2 = np.array([[30,2], [27,3], [22,2], [21,1], [18,2], [17,1], [17,1], [14,2], [13,1], [10,2], [9,1], [7,3], [3,3], [2,1], [17,2], [17,3], [15,3], [15,1], [15,2], [15,3], [14,2], [14,1], [14,3]])
berryLabels2 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,2,2,1,1,2,2])
berryFeaturesCache2 = np.array([[32,5]])
#berryFeatures = np.array([[]])
#berryLabels = np.array([[]])

berryFeaturesCon1 = np.array("berryfeatures2.csv")
berryLabelsCon1 = np.array ("berrylabels2.csv")
berryFeaturesCon2 = np.array("berryfeatures2.csv")
berryLabelsCon2 = np.array ("berrylabels2.csv")

Winner1 = 2
Winner2 = 2

print ("welcome to nim!")

#global var
p1Wins = 0
p2Wins = 0
generation = 0

#displays the number of berries 
def display(berries):
    pile = []
    counter = 0
    while counter < berries:
        pile.append("O")
        counter += 1
    
    print("\n")
    print(pile)
    print(berries)
    return(pile)

#turn player one
def pturnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2):
    global playerselect
    print("Player 1's turn!")
    
    reduction = input("How many berries will you take? (1, 2, or 3?) ")
    
    if reduction != '1' and reduction != '2' and reduction != '3':
        print ("Invalid input, try again loser")
        pturnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    
    berries = berries - int(reduction)
    
    if berries <= 0:
        print("Player 1 won!")
        Winner2 = 2
        p1Wins += 1
        if playerselect == '1':
            learnSht(berryFeatures1, berryLabels1, berryFeaturesCache1, berryFeatures2, berryLabels2, berryFeaturesCache2, Winner1, Winner2, p1Wins, p2Wins)
        else:
            quit()
        

    display(berries)

    
    if playerselect == '2':
        pturntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    else:
        turntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)

#turn player  two
def pturntwo (berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2):
    print("Player 2's turn!")
    reduction = input("How many berries will you take? (1, 2, or 3?) ")
    
    if reduction != '1' and reduction != '2' and reduction != '3':
        print ("Invalid input, try again loser")
        pturntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    
    berries = berries - int(reduction)
    
    if berries <= 0:
        print("Player 2 won!")
        #quit()

    display(berries)

    global playerselect
    pturnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    
#turn one
def turnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2):
    print("Computer 1's turn!")
    if clf1.predict([[berries,1]]) == 1:
        reduction = 1
    elif clf1.predict([[berries,2]]) == 1:
        reduction = 2
    elif clf1.predict([[berries,3]]) == 1:
        reduction = 3
    #elif berries % 4 != 0:
        #reduction = berries % 4
    else:
        reduction = random.randint(1,3)
    #print(str(berries) + " " + str(reduction))
    berryFeaturesCache1 = np.concatenate((berryFeaturesCache1, [[berries, reduction]]), axis = 0)
    #print(berryFeaturesCache)

    
    berries = berries - int(reduction)
    print("Computer 1 took " + str(reduction))
    
    if berries <= 0:
        print("Computer 1 won!")
        Winner1 = 2
        Winner2 = 1
        p1Wins += 1
        learnSht(berryFeatures1, berryLabels1, berryFeaturesCache1, berryFeatures2, berryLabels2, berryFeaturesCache2, Winner1, Winner2, p1Wins, p2Wins)

    display(berries)

    turntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)

#turn two
def turntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2):
    print("Computer 2's turn!")
    if clf2.predict([[berries,1]]) == 1:
        reduction = 1
    elif clf2.predict([[berries,2]]) == 1:
        reduction = 2
    elif clf2.predict([[berries,3]]) == 1:
        reduction = 3
    #elif berries % 4 != 0:
        #reduction = berries % 4
    else:
        reduction = random.randint(1,3)
    #print(str(berries) + " " + str(reduction))
    berryFeaturesCache2 = np.concatenate((berryFeaturesCache2, [[berries, reduction]]), axis = 0)
    #print(berryFeaturesCache)

    
    berries = berries - int(reduction)
    print("Computer 2 took " + str(reduction))
    
    if berries <= 0:
        print("Computer 2 won!")
        Winner1 = 2
        Winner2 = 1
        p2Wins += 1
        learnSht(berryFeatures1, berryLabels1, berryFeaturesCache1, berryFeatures2, berryLabels2, berryFeaturesCache2, Winner1, Winner2, p1Wins, p2Wins)

    display(berries)

    global playerselect
    if playerselect == '0':
        turnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    else:
        pturnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)

    
#set up for game start
def gameStart(berryFeatures1, berryLabels1, berryFeatures2, berryLabels2, p1Wins, p2Wins):
    print("Score (P1 | P2): " + str(p1Wins) + " | " + str(p2Wins))
    global generation
    generation += 1
    print("Generation " + str(generation))
    #print(len(berryLabels))
    berries = random.randint(15, 30)
    pile = []
    clf1 = svm.SVC(kernel='rbf', gamma = 2, C = 2)
    #clf1 = tree.DecisionTreeClassifier()
    clf1 = clf1.fit(berryFeatures1, berryLabels1)
    prettyPicture(clf1, berryFeaturesCon1, berryLabelsCon1)
    clf2 = svm.SVC(kernel='rbf', gamma = 2, C = 2)
    #clf2 = tree.DecisionTreeClassifier()
    clf2 = clf2.fit(berryFeatures2, berryLabels2)
    prettyPicture(clf2, berryFeaturesCon2, berryLabelsCon2)
    display(berries)

    with open ("berryfeatures1.csv", "a") as f:
        bfeatures1 = csv.writer(f, dialect = "excel",quoting=csv.QUOTE_NONNUMERIC)
        bfeatures1.writerow(berryFeatures1)
    
    with open ("berrylabels1.csv", "a") as g:
        blabels1 = csv.writer(g, dialect = "excel", quoting=csv.QUOTE_NONNUMERIC)
        blabels1.writerow(berryLabels1)
    
    with open ("berryfeatures2.csv", "a") as f:
        bfeatures2 = csv.writer(f, dialect = "excel",quoting=csv.QUOTE_NONNUMERIC)
        bfeatures2.writerow(berryFeatures2)
    
    with open ("berrylabels2.csv", "a") as g:
        blabels2 = csv.writer(g, dialect = "excel", quoting=csv.QUOTE_NONNUMERIC)
        blabels2.writerow(berryLabels2)

    global playerselect
    if playerselect == "0":
        if random.randint(1,2) == 1:
            turnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
        else:
            turntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    elif playerselect == "2":
        if random.randint(1,2) == 1:
            pturnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
        else:
            pturntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    else:
        if random.randint(1,2) == 1:
            pturnone(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
        else:
            turntwo(berries, pile, clf1, clf2, p1Wins, p2Wins, berryFeaturesCache1, berryFeatures1, berryLabels1, berryFeaturesCache2, berryFeatures2, berryLabels2)
    

def learnSht(berryFeatures1, berryLabels1, berryFeaturesCache1, berryFeatures2, berryLabels2, berryFeaturesCache2, Winner1, Winner2, p1Wins, p2Wins):
    gameLength = len(berryFeaturesCache1)
    #print(gameLength)
    #print(berryFeatures)
    
    #print(berryFeaturesCache)
    berryFeatures1 = np.concatenate((berryFeatures1, berryFeaturesCache1), axis = 0)
    count2 = 0
    while count2 < gameLength:
        berryLabels1 = np.concatenate((berryLabels1, [Winner1]), axis = None)
        count2 += 1
        #print(count2)
        #print(berryLabels)
    berryFeaturesCache1 = np.array([[]])



    gameLength = len(berryFeaturesCache2)
    berryFeatures2 = np.concatenate((berryFeatures2, berryFeaturesCache2), axis = 0)
    count2 = 0
    while count2 < gameLength:
        berryLabels2 = np.concatenate((berryLabels2, [Winner2]), axis = None)
        count2 += 1
        #print(count2)
        #print(berryLabels)
    berryFeaturesCache2 = np.array([[]])

    gameStart(berryFeatures1, berryLabels1, berryFeatures2, berryLabels2, p1Wins, p2Wins)

playerselect = '0'

def playernum():
    global playerselect
    playerselect = input("How many players? (0, 1, or 2) ")
    if playerselect != '1' and playerselect != '2' and playerselect != '0':
        print ("Invalid input, try again")
        playernum()

playernum()
gameStart(berryFeatures1, berryLabels1, berryFeatures2, berryLabels2, p1Wins, p2Wins)
    