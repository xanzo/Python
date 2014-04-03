#!/usr/bin/python2

"""
DBDM Exam 2013 - sqlite example
"""

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plot

__author__='Jensen, Casper Radmer'
__version__='1.0'
__modified__='20140403'


# open connection to database, create cursor
sqlserver = sql.connect("DataminingAssignment2014.db")
cursor = sqlserver.cursor()

# execute sql-statement
tables = cursor.execute('select y from SSFR_Train_Y').fetchall()

print "Opgave 1.2"
#opgave 1.2 a
#Finds the average
sammenlagt = 0
avg = 0

for row in tables:
  sammenlagt = sammenlagt + row[0]

avg = sammenlagt / len(tables)
print ""
print "Average:", avg

#opgave 1.2 b
#Finds the average, where the average has been subtracted from each row
sammenlagt = 0
raekke = 0

for row in tables:
  raekke = (row[0] - avg) * (row[0] - avg)
  sammenlagt = sammenlagt + raekke

print "Average from, (row - average) to each row: ", sammenlagt / len(tables)

print ""
print "Opgave 1.3.1"
#Opgave 1.3.1
#Adding b to x and finds w.T * x + b (five parameters)
y = np.matrix(cursor.execute('select y from SSFR_Train_Y').fetchall())
x = np.matrix(cursor.execute('select x1,x2,x3,x4 from SSFR_Train_X').fetchall())
x = np.insert(x, 4, 1, axis = 1) #indsætter i hvad (x), i hvilken række/søjle (4), hvad der skal indsættet (1), og om række/søjle (axis = 1)
w = (x.T * x).I * x.T * y

print w

print ""
print "Opgave 1.3.2"
#Opgave 1.3.2
#Deletes b from x but keep the five parameters as w and b
x = np.delete(x, 4, axis = 1)
w = np.matrix([[-0.79400153],[-1.2229592],[-0.32858475],[-0.78633056]])
b = -8.14943349

#Finds the mean-sqared-error for train
counter = 0
J = 0
while counter < len(y):
    J = J + (y[counter] - (w.T * x[counter].T + b))**2
    counter = counter + 1
    
print J / len(y)

print ""
print "Opgave 1.3.3"
#Opgave 1.3.3
#Finds the mean-sqared-error for test
y = np.matrix(cursor.execute('select y from SSFR_Test_Y').fetchall())
x = np.matrix(cursor.execute('select x1,x2,x3,x4 from SSFR_Test_X').fetchall())

w = np.matrix([[-0.79400153],[-1.2229592],[-0.32858475],[-0.78633056]])
b = -8.14943349

counter = 0
J = 0
while counter < len(y):
    J = J + (y[counter] - (w.T * x[counter].T + b))**2
    counter = counter + 1
    
print J / len(y)

print ""
print "Opgave 2.1"
'''
#Opgave 2.1
test_x = np.matrix(cursor.execute('select x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 from Objects_Test_X').fetchall())
test_y = np.matrix(cursor.execute('select y from Objects_Test_Y').fetchall())
train_x = np.matrix(cursor.execute('select x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 from Objects_Train_X').fetchall())
train_y = np.matrix(cursor.execute('select y from Objects_Train_Y').fetchall())

#Making a list of which is galaxies and which is stars
galaxies_and_stars = []
counter_test = 0
counter_train = 0

while counter_test < len(test_x):
  nearest_dist = None
  nearest_t = None
  while counter_train < len(train_x):
    dist = np.linalg.norm(test_x[counter_test] - train_x[counter_train])
    if nearest_dist == None or dist < nearest_dist:
      nearest_dist = dist
      nearest_t = train_y[counter_train]
    counter_train = counter_train + 1
  galaxies_and_stars.append(nearest_t)
  counter_train = 0
  counter_test = counter_test + 1

#Checks hwo many corrects there are
corrects = 0
count = 0
while count < len(test_y):
  if galaxies_and_stars[count] == test_y[count]:
    corrects = corrects + 1
  count = count + 1

print (float(corrects) / len(test_y)) * 100
'''

print ""
print "Opgave 2.2"
#Opgave 2.2
x = np.matrix(cursor.execute('select x0,x1,x2,x3,x4,x5,x6,x7,x8,x9 from Objects_Train_X').fetchall())
y = np.matrix(cursor.execute('select y from Objects_Train_Y').fetchall())

#Making a list of all galaxies and finds the average of each column
galaxies = []
count = 0
while count < len(y):
  if y[count] == 0:
    galaxies.append(x[count])
  count = count + 1

avg = (np.mean(galaxies, axis = 0)).T

#Finds the eigenspectrum
counter = 0
sum = np.zeros(shape=(10,10))
while counter < len(galaxies):
  sum = sum + (galaxies[counter] - avg) * (galaxies[counter] - avg).T
  counter = counter + 1

galaxies_avg = sum / len(galaxies)

eig = np.linalg.eig(galaxies_avg)

eig_value = eig[0]
eig_vector = eig[1]

counter2 = 0
sum2 = np.zeros(shape=(10,10))
while counter2 < len(galaxies):
  sum2 = sum2 + eig_vector.T * (galaxies[counter2] - avg)
  counter2 = counter2 + 1

print "plot: check picture 1"
plot.plot(eig_value)
plot.show()

#Finds how many components are necessary to fill 90%
eig_value_sum = 0
counter3 = 0
while counter3 < len(eig_value):
  eig_value_sum = eig_value_sum + eig_value[counter3]
  counter3 = counter3 + 1

ninety_procent = eig_value_sum * 0.9

amount = 1
counter4 = 0
sum = 0
while sum < ninety_procent:
  sum = sum + eig_value[counter4]
  amount = amount + 1
  counter4 = counter4 + 1

print ""
print "amount of components for minimum 90%:", amount
print ""
print "scatter plot for the first two components: check picture 2"

#Making the scatter plot of the first two components
plot.plot([1,2],[eig_value[0],eig_value[1]], 'ro')
plot.axis([0.5,2.5,200,500])
plot.show()

print ""
print "Opgave 2.3"
#Opgave 2.3


# close cursor, connection to database
cursor.close()
sqlserver.close()
