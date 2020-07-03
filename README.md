# Machine Learning Python

**This repo contains all models that I wrote during learning Data Science - Machine Learning**

> I am making these files for my learning purpose so some things may get repeated as I reach advance level for those topics.

*These are just basic format of making these models and nothing new*

Both .py and .ipynb files are added

> *In case of any confusion on using libraries, check their documentations:*
> - [***pandas***](https://pandas.pydata.org/docs/reference/index.html)
> - [***numpy***](https://numpy.org/doc/)
> - [***matplotlib***](https://matplotlib.org/contents.html)
> - [***scikit learn***](https://scikit-learn.org/stable/modules/classes.html)


### Information on Libraries used

> - **pandas** 		: It provides fast, expressive, and flexible data structures to easily work with structured and time-series data.
> - **numpy** 		: It has advanced math functions and a rudimentary scientific computing package.
> - **matplotlib** 	: Matplotlib helps with data analyzing, and is a numerical plotting library.
> - **sklearn** 	: Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface

##### Modules

>pandas

>numpy

>matplotlib
>	- pyplot
>	- colors

>sklearn
>	- impute
>	- compose
>	- preprocessing
>	- model_selection
>	- linear_model
>	- svm
>	- tree
>	- ensemble
>	- metrics
>	- neighbors

##### Classes

>pandas

>numpy

>matplotlib
>	- colors
>		- ListedColormap

>sklearn
>	- impute
>		- SimpleImputer(missing_values, strategy)
>	- compose
>		- ColumnTransformer(transformers = [(transform_type, encoder_used, column_index)], remainder)
>	- preprocessing
>		- LabelEncoder()
>		- OneHotEncoder()
>		- StandardScalar()
>		- PolynomialFeatures(degree)
>	- linear_model
>		- LinearRegression()
>		- LogisticRegression()
>	- svm
>		- SVR(kernel)
>		- SVC(kernel)
>	- tree
>		- DecisionTreeRegressor(random_state)
>	- ensemble
>		- RandomForestRegressor(n_estimators, random_state)
>	- neighbors
>		- KNeighborsClassifier(n_neighbors, metric, p)

##### Functions / Methods

>pandas
>	- . 
>		- .
>			- read_csv('file.csv')
>			- iloc[rows, :columns]
>			- values

>numpy
>	- .
>		- .
>			- array()
>			- set_printoptions(precision)
>			- reshape(row, column)
>			- concatenate((array_1, ..., array_n), axis)
>			- arange(min(x), max(x), 0.1)

>matplotlib
>	- pyplot
>		- .
>			- scatter(x, y, color)
>			- plot(x, y, color)
>			- title('')
>			- xlabel('')
>			- ylabel('')
>			- show()
>			- legend()
>			- xlim()
>			- ylim()
>			- contourf()

>sklearn
>	- impute
>		- SimpleImputer(missing_values, strategy)
>			- fit(array)
>			- transform(array)
>	- *All Types*
>		- .
>			- fit
>			- transform
>			- inverse_transform
>			- fit_transform
>	- model_selection
>		- .
>			- train_test_split(x, y, test_size, random_state)
>	- linear_model
>		- LinearRegression
>			- fit(x, y)
>			- predict(x)
>			- coef
>			- intercept
>	- metrics
>		- .
>			- confusion_matrix
>			- accuracy_score