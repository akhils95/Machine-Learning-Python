'''
Polynomial Regression

Polynomial Linear Regression follows the equation: y = b0 + b1*x^2 + b2*x^2 + ... + bn*x^2 so it is not a straight line.
We have a small data here and since we need to predict thr salary we will not split the data in this case.
We are doing both linear and polinomial to compare the results.
'''

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:-1].values					# We are excluding the 1st column as those strings are not needed
y = dataset.iloc[:, -1].values

# Training the Linear Regression model on the whole dataset

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Training the Polynomial Regression model on the whole dataset

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)			# This class will be used to turn the matrix of x into a matrix of x and x^2
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()						# We are just runing the linear regression on the matrix of squares
lin_reg_2.fit(x_poly, y)

# Visualising the Linear Regression results

plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg.predict(x), color = 'blue')
plt.title('Linear Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results

plt.scatter(x, y, color = 'red')					# The plot will be more accurate depending on our polynomial degree set above
plt.plot(x, lin_reg_2.predict(x_poly), color = 'blue')
plt.title('Polynomial Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)

x_grid = np.arange(min(x), max(x), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, lin_reg_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression

print('\nThe salary for employee applying for level 6.5 using SLR is')
print(lin_reg.predict([[6.5]])[0])

# Predicting a new result with Polynomial Regression

print('\nThe salary for employee applying for level 6.5 using PLR is')
print(lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))[0])