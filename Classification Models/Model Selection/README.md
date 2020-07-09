# Model Selection for Classification Models

We have already made all these models but we tested them on a small dataset with two variables only. Our new dataset is quite large with over 600 rows and contains many variables.

Since our data has more than two variables there is no graph plotting added.

Also we are not predicting the category, we are just checking the accuracy of predictions for all models on this dataset.

This is the most basic template for these models.

| **MODEL**                    | **Accuracy** | **Accuracy from previous data** |
|------------------------------|--------------|---------------------------------|
| Logistic Regression          | 94.7%        | 89%                             |
| K Nearest Neighbor           | 94.7%        | 93%                             |
| Support Vector Machine       | 94.1%        | 90%                             |
| Kernel SVM                   | 95.3%        | 93%                             |
| Naive Bayes                  | 94.1%        | 90%                             |
| Decision Tree Classification | 95.9%        | 91%                             |
| Random Forest Classification | 93.5%        | 91%                             |

As you can see accuracy of each model is different for different datasets. We can always check the accuracies for different data before deciding which model to choose.