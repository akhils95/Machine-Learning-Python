'''
An SVR is plotted like a Linear Regression only, except that there is an area parallel to the line equally on both sides considered to
neglect errors. The points outside this area are the ones that gives us the line and are called support vectors (ξ).
The tube around the line is ϵ on both side parallel to y axis and the points outside are denoted by ξ above the line
and ξ* below the line
'''

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values					# We are excluding the 1st column as those strings are not needed
y = dataset.iloc[:, -1].values
y = y.reshape(len(y), 1)							# y is required as a 2d array with salaries recorded vertically in column
# Reshaping of y is done as standardisation class require that for scaling

# Feature Scaling

'''
In SVR we have an implicit equation, so we dont have any coefficients compensating for the higher or lower values
Thus feature scaling is required.
It is to be noted that feature scaling is derived from trainning set only but this is an exceptional case
Also here we dont have 1's and 0's as our dependents, so we will apply scaling to them also.
'''

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x = sc_x.fit_transform(x)
sc_y = StandardScaler()				# The instance sc_x contains mean and standard deviation of x, so we create a new one for y.
y = sc_y.fit_transform(y)

# Training the SVR model on the whole dataset

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf') 	# Kernels will be taught later 
regressor.fit(x, y)

# Predicting a new result

'''
We transform the value we want to check for into a 2d array by putting it within[[]], then we put it on same scale as our trained values
We apply the predict method on that and then inverse transform to get actual value on y from the scale
'''

print(sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]])))[0])

# Visualising the SVR results

plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = 'red')					
plt.plot(sc_x.inverse_transform(x), sc_y.inverse_transform(regressor.predict(x)), color = 'blue')
plt.title('SVR Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)

x_grid = np.arange(min(sc_x.inverse_transform(x)), max(sc_x.inverse_transform(x)), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(sc_x.inverse_transform(x), sc_y.inverse_transform(y), color = 'red')
plt.plot(x_grid, sc_y.inverse_transform(regressor.predict(sc_x.transform(x_grid))), color = 'blue')
plt.title('SVR Model')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()