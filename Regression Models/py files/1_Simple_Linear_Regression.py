'''
Simple Linear Regression follows the equation of straight line: y = b0 + b1*x
y -> Dependent Variable
x -> Independent Variable
b1 -> Coefficient of change
b0 -> Constant

This model will find the best fitting line for a data. For each y it will test different values of y^ that form a straight line.
Then it will look for the minimum value of som of all squares of (y-y^). That set of y^ values will give the best fitting line.
'''

# We are splitting this file in two parts: The preprocessing data part that we already know and the prediction part of this model

# PART 1 --------------------------------------------------------------------------------------------------

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# PART 2 --------------------------------------------------------------------------------------------------

# Training the Simple Linear Regression model on the Training set

'''For training we will use LinearRegression class from linear_model module of sklearn'''

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the Test set results

'''In this part we test our trained model with our test set usin the predict method'''

y_pred = regressor.predict(x_test)

# Visualising the Training set results

'''
We will be using matplotlib to plot graph
First we will use scatter function from pyplot module to plot the training data or the given data
Then we plot regression line using plot function
We can also give a title to the graph using the title function
We will specify the x-axis and y-axis labels using functions xlabel and ylabel
Finally we will display the graph by calling the show function
'''

plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary v/s Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
'''
We dont change the regression line parameters from train to test as the regression line remains the same
'''

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary v/s Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Bonus Part ----------------------------------------------------------------------------------------

'''
Making a single prediction
Making a single prediction
(for example salary for employee with an experience of 12 years)
'''

print('\nThe salary for employee with an experience of 12 years is')
print(regressor.predict([[12]])[0])

'''
Getting the final linear regression equation with the values of the coefficients
'''

co = (regressor.coef_)
b = (regressor.intercept_)

print('\nEquation for this regression is')
print(f'Salary = {co[0]} x Experience + {b}')