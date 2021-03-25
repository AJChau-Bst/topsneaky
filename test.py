#import tbapy
import numpy as np
import matplotlib.pyplot as plt
import csv
#import pandas
#import statsmodels
#import seaborn
#import plotly
import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import random

from class_vis import prettyPicture, output_image

berryFeatures = np.array([[30,2], [27,3], [22,2], [21,1], [18,2], [17,1], [17,1], [14,2], [13,1], [10,2], [9,1], [7,3], [3,3], [2,1], [17,2], [17,3], [15,3], [15,1], [15,2], [15,3], [14,2], [14,1], [14,3]])
berryLabels = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,2,2,1,1,2,2])
#berryFeatures = np.array([[]])
#berryLabels = np.array([[]])
berryFeaturesCache = np.array([[32,5]])

Winner = 2

#print(clf.predict([[29,1]]))
#print(clf.predict([[29,2]]))
#print(clf.predict([[29,3]]))



#print("fuck")
#ohno = input("How's ya fucking day? ")

#print (ohno)
#if(ohno=="bad"):
#    

print ("welcome to nim, you nerd.")

pWins = 0
cWins = 0
generation = 0

def display(berries):
    pile = []
    counter = 0
    while counter < berries:
        pile.append("O")
        counter += 1
    print(pile)
    print(berries)
    return(pile)

#playerturn = 1

#def turnover(playerturn,berries,pile): 
#    if playerturn==1:
#        print("Player 1's turn!")
#    else:
#        print("Player 2's turn!")
#    
#    if reduction != '1' and reduction != '2' and reduction != '3':
#        print ("Invalid input, try again loser")
#        turnover(playerturn,berries,pile)
#        
#    
#    berries = berries - int(reduction)
#    
#    if berries == 0:
#        print("Player " + str(playerturn) + " won!")
#        print("ha. sucker")
#        print("NERDDDDD")
#        quit()
#    elif berries < 0:
#        berries = berries + int(reduction)
#        turnover(playerturn,berries,pile)
#
#    display(berries)
#
#    if playerturn==1:
#        playerturn = 2
#    else:
#        playerturn = 1
#    turnover(playerturn,berries,pile)

def turnone(berries, pile, clf, pWins, cWins, berryFeaturesCache, berryFeatures, berryLabels):
    print("Player 1's turn!")
    reduction = input("How many berries will you take? (1, 2, or 3?) ")
    
    if reduction != '1' and reduction != '2' and reduction != '3':
        print ("Invalid input, try again loser")
        turnone(berries, pile, clf, pWins, cWins, berryFeaturesCache, berryFeatures, berryLabels)
    
    berries = berries - int(reduction)
    
    if berries <= 0:
        print("Player won!")
        Winner = 2
        pWins += 1
        learnShit(berryFeatures, berryLabels, berryFeaturesCache, Winner, pWins, cWins)

    display(berries)

    turntwo(berries,pile,clf, pWins, cWins, berryFeaturesCache, berryFeatures, berryLabels)

def turntwo(berries, pile, clf, pWins, cWins, berryFeaturesCache, berryFeatures, berryLabels):
    print("Computer's turn!")
    if clf.predict([[berries,1]]) == 1:
        reduction = 1
    elif clf.predict([[berries,2]]) == 1:
        reduction = 2
    elif clf.predict([[berries,3]]) == 1:
        reduction = 3
    #elif berries % 4 != 0:
        #reduction = berries % 4
    else:
        reduction = random.randint(1,3)
    #print(str(berries) + " " + str(reduction))
    berryFeaturesCache = np.concatenate((berryFeaturesCache, [[berries, reduction]]), axis = 0)
    #print(berryFeaturesCache)
    
    berries = berries - int(reduction)
    print("Computer took " + str(reduction))
    
    if berries <= 0:
        print("Computer won!")
        print("ha. sucker")
        print("NERDDDDD")
        Winner = 1
        cWins += 1
        learnShit(berryFeatures, berryLabels, berryFeaturesCache, Winner, pWins, cWins)

    display(berries)

    turnone(berries, pile, clf, pWins, cWins, berryFeaturesCache, berryFeatures, berryLabels)

def gameStart(berryFeatures, berryLabels, pWins, cWins):
    print("Score (P|C): " + str(pWins) + " | " + str(cWins))
    global generation
    generation += 1
    print("Generation " + str(generation))
    #print(len(berryLabels))
    berries = 17
    pile = []
    clf = svm.SVC(kernel='rbf', gamma = 2, C = 2)
    clf = clf.fit(berryFeatures, berryLabels)
    prettyPicture(clf, berryFeatures, berryLabels)
    display(berries)
    turntwo(berries, pile, clf, pWins, cWins, berryFeaturesCache, berryFeatures, berryLabels)

def learnShit(berryFeatures, berryLabels, berryFeaturesCache, Winner, pWins, cWins):
    gameLength = len(berryFeaturesCache)
    #print(gameLength)
    #print(berryFeatures)
    
    #print(berryFeaturesCache)
    berryFeatures = np.concatenate((berryFeatures, berryFeaturesCache), axis = 0)
    count2 = 0
    while count2 < gameLength:
        berryLabels = np.concatenate((berryLabels, [Winner]), axis = None)
        count2 += 1
        #print(count2)
        #print(berryLabels)
    berryFeaturesCache = np.array([[]])
    gameStart(berryFeatures, berryLabels, pWins, cWins)

gameStart(berryFeatures, berryLabels, pWins, cWins)
    