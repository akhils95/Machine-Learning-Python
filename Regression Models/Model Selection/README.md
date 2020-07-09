# Evaluating different models for your data

As we know, the model with the r-squared value closest to 1 is the best working model. We have here our five main models working on same dataset. We will *compare there r-squared values* using *scikit learn library* to figure out which is best for our data.

We have not included the single linear regression here as
	- We have a data with multiple variables
	- It won't be used in real life scenarios.

The data is from the [**UCI Machine Learning Repository**](https://archive.ics.uci.edu/ml/index.php), which provides various real life datasets for us to practice machine learning on.

[*Click here*](https://scikit-learn.org/stable/modules/classes.html) to get documentation for scikit learn library.

## Understanding our Data

- We do not need to concern ourself with the physics of the dataset, just understand the dependency.
- This dataset have no categorical data or missing values and have a little less than 10000 values.
- We have a dataset of first four columns containing values for **Temperature, Vaccum, Pressure and Humidity**; these are our **independent variables**.
- Then we have the fifth column containing values for the **Energy Output**, which is our **dependent variable**.

## The comparision

On running the last code for evaluating the r-squared values

`from sklearn.metrics import r2_score`

`r2_score(y_test, y_pred)`


We get the following result:

| REGRESSION MODEL             | r-squared value    |
|------------------------------|--------------------|
| Multiple Linear Regression   | 0.9325315554761303 |
| Polynomial Linear Regression | 0.9458193390165572 |
| Support Vector Regression    | 0.9480784049986258 |
| Decision Tree Regression     | 0.9226091050550043 |
| Random Forest Regression     | 0.9615980699813017 |

###### From the accuired results we can conclude that Random Forest Regression is the best model for this data.
