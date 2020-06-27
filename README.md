# Machine-Learning-Python

**This repo contains all models that I wrote during learning Data Science - Machine Learning**

*These are just basic format of making these models and nothing new*

Both .py and .ipynb files are added

***

### Information on Libraries used

>**pandas** 				It provides fast, expressive, and flexible data structures to easily work with structured and time-series data.
>**numpy** 				It has advanced math functions and a rudimentary scientific computing package.
>**matplotlib** 			Matplotlib helps with data analyzing, and is a numerical plotting library.
>**sklearn** 			Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface

##### Modules

>pandas

>numpy

>matplotlib
>	pyplot

>sklearn
>	impute
>	compose
>	preprocessing
>	model_selection
>	linear_model
>	svm
>	tree
>	ensemble

##### Classes

>pandas

>numpy

>matplotlib

>sklearn
>	impute
>		SimpleImputer(missing_values, strategy)
>	compose
>		ColumnTransformer(transformers = [(transform_type, encoder_used, column_index)], remainder)
>	preprocessing
>		LabelEncoder()
>		OneHotEncoder()
>		StandardScalar()
>		PolynomialFeatures(degree)
>	linear_model
>		LinearRegression()
>	svm
>		SVR(kernel)
>	tree
>		DecisionTreeRegressor(random_state)
>	ensemble
>		RandomForestRegressor(n_estimators, random_state)

##### Functions / Methods

>pandas
>	read_csv('file.csv')				# Gets data from a csv file
>	iloc[rows, :columns]				# Get index locations of given rows and columns
>	values 								# Get values for given index

>numpy
>	array()								# Converts data into a numpy array
>	datatype 							# Returns all of that variable type(eg. numpy.nan returns all nan datatypes)
>	set_printoptions(precision) 		# Sets a limit to decimal values
>	reshape(row, column)				# To reshape a matrix
>	concatenate((array_1, ..., array_n), axis)
>	arange(min(x), max(x), 0.1)			# Arrange integers as floats with 0.1 difference

>matplotlib
>	pyplot
>		scatter(x, y, color)
>		plot(x, y, color)
>		title('')
>		xlabel('')
>		ylabel('')
>		show()

>sklearn
>	impute
>		SimpleImputer(missing_values, strategy)
>			fit(array)
>			transform(array)
>	All Types
>		fit
>		transform
>		inverse_transform
>		fit_transform
>	model_selection
>		train_test_split(x, y, test_size, random_state)
>	linear_model
>		LinearRegression
>			fit(x, y)
>			predict(x)					# x is a 2d array
>			coef						# Returns all coefficients
>			intercept 					# Returns the intercept