'''
Multiple Linear Regression also follows a straight line equation
Unlike Simple Linear Regression, it has more than one independent Variables
y = b0 + b1*x1 + b2*x2 + ... + bn*xn
Our data contains information regarding 50 anonymous startups containing their spends(3), location and profits
'''

# PART 1 ------------------------------------------------------------------------------------------

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('50_Startups.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encoding categorical data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
x = np.array(ct.fit_transform(x))

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# PART 2 ------------------------------------------------------------------------------------------

'''
We will Build as well as train out predicting model here.
This process can easily be done by the LinearRegression method which takes care of dummy variable trap and Variable significance
'''

# Training the Multiple Linear Regression model on the Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predicting the Test set results

'''
Since we have too many independent variables we cannot really plot a graph.
So, we will display the predictd test values with the known test values to see a comparision
For beeter display we are using numpy library to set decimal precision to 2
We used the reshape function to make our vectors vertical entering params row=length wich is originally column and 
column = 1 so our syntax is reshape(row, column)
we also used numpy's concatenate function to join aor test and prediction vector together by giving as params both arrays as tuple
Then we entered axis = 1 for horizontal concatination, for vertical axis is 0 so syntax is concatenate((array1, array 2), axis)
'''

y_pred = regressor.predict(x_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# Bonus Part --------------------------------------------------------------------------------------

'''
Making a single prediction
(for example the profit of a startup with R&D Spend = 160000, Administration Spend = 130000, Marketing Spend = 300000 and State = 'California')
'''

print('\nThe profit if state is California, Spend for R&D = 160000, Administration = 130000, Marketing = 300000 is')
print(regressor.predict([[1, 0, 0, 160000, 130000, 300000]])[0])

'''
Getting the final linear regression equation with the values of the coefficients
'''

co = (regressor.coef_)
b = (regressor.intercept_)

print('\nEquation for this regression is')
print(f'Profit = {co[0]} x State 1 + {co[1]} x State 2 + {co[2]} x State 3 + {co[3]} x R&D + {co[4]} x Administration + {co[5]} x Marketing + {b}')