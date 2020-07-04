# Theory knowledge necesarry for Data Science.

This is a markdown file containing information about all models that we have built and also some small mathematical processess that may have happened in between.

---

## Table of contents:

| Topic                 |                                |
|-----------------------|--------------------------------|
| Data Preprocessing    | [Jump](#data-preprocessing)    |
| Regression Models     | [Jump](#regression-models)     |
| Classification Models | [Jump](#classification-models) |

---

### Data Preprocessing

The first step to any data science model is preprocessing the data. This includes:  
* Importing data from a csv file.
* Getting dependent and independent variables from that data.
* Encoding any categorical data if present.
* Taking care of any missing values.
* Spliting the data into trainning and test set.
* Apllying feature scaling if needed.

Most of the points of data processing are prety straight forward. So, we will only talk about how *missing values* are taken care of and the *feature scaling* just to undertand the concept

When there is a value missing in our data it can affect our whole model predictions so we generally take care of that using the mean of that whole column but other methods like using meadian can also be used.

Feature scaling is done to bring the whole data on similar scale so that the model don't neglect some values due to the huge difference in values. For example if we have two columns like age and salary, the model may not consider age as it would be a two digit number while salaries would be in thousands.  

We have two ways of doing feature scaling -
* Standardization  
* Normalization

![Standardization and normalization formula](/images/Standard-Normal.jpg)

### Regression Models



### Classification Models