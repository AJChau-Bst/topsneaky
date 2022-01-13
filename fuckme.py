import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

#Lists!
Team = []
OPR = []
DPR = []
CCWM = []

#Requests
request = input("team number")
request = "frc" + request

yearrequest = input("year you want data from")

#basic plot stuff
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

#puts stuff in lists
with open(yearrequest + '.csv') as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:
        Team.append(row[0])
        OPR.append(row[1])
        DPR.append(row[2])
        CCWM.append(row[3])
    #remove the header
    Team.remove(Team[0])
    OPR.remove(OPR[0])
    DPR.remove(DPR[0])
    CCWM.remove(CCWM[0])

    #turn everything into an integer for plotting
    OPR = [ float(x) for x in OPR ]
    DPR = [ float(x) for x in DPR ]
    CCWM = [ float(x) for x in CCWM ]

#defining to plot
x = OPR
y = DPR
z = CCWM

#actualy plotting now
ax.scatter(x, y, z, s=3, c='r', marker='*')

exprime = Team.index(request)

#identify the OPR DPR and CCWM position

a = OPR[exprime]
b = DPR[exprime]
c = CCWM[exprime]


#print OPR, DPR and CCWM of specified team
print("OPR, DPR, CCWM")
print(a, b, c)

ax.scatter(a, b, c, s=10, c='b', marker='s')


ax.set_xlabel('OPR')
ax.set_ylabel('DPR')
ax.set_zlabel('CCWM')
plt.show()