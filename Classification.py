import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

# Reading the data
data = pd.read_csv('covid19_Final.csv')
# Filtering the data and removing the dates after getting the difference between them in days using Excel
data.drop(['date_onset_symptoms', 'date_confirmation', 'date_admission_hospital'],axis=1 ,inplace=True)

# Converting the output into numeric classes
data['outcome'].replace({"discharge": 1, "death": 2, "stable": 3,"severe": 4}, inplace=True)
# Save a new CSV File with the data that has all numeric values
data.to_csv('FinalData.csv', index= False)

# define my target/output value
y = data.outcome
# splitting data 70% and 30%
x_train, x_test, y_train, y_test = train_test_split(data, y, test_size=0.3)

# Building the MLP
ANN = MLPClassifier(solver= 'lbfgs', alpha= 1e-5, hidden_layer_sizes=(10), random_state=1, activation= 'relu')
# Training the MLP
ANN.fit(x_train, y_train)
# Testing MLP
r = ANN.predict(x_test)
# Checking the testing classification accuracy
a = r == y_test
true = 0
false = 0
for i in a:
    if i:
        true += 1
    elif not i:
        false += 1
ANN_acc = (true/len(y_test)) * 100
# printing the reults
print("\nMultilayer perceptron accuracy is: ", false, " False predictions and ", true, " True Predictions, with accuracy of ", ANN_acc)
print("Confusion Matrix MLP: ")
print(confusion_matrix(r, y_test))
# Printing precision,accuracy and f measure
print(classification_report(y_test,r, zero_division= 0))


# Building the support vector machine
SVM = svm.SVC(kernel="linear")
# Training SVM
SVM.fit(x_train, y_train)
# Testing SVM
SVM_Pred = SVM.predict(x_test)

# Getting the accuracy of the testing classification
ress = (SVM_Pred == y_test)
true_S = 0
false_S = 0
for v in ress:
    if v:
        true_S += 1
    elif not v:
        false_S += 1
SVM_acc = (true_S/len(y_test)) * 100
# Printing the final results
print("\nSupport vector machine accuracy is: ", false_S, " False predictions and ", true_S, " True Predictions, with accuracy of ", SVM_acc)
print("Confusion Matrix SVM: ")
print(confusion_matrix(SVM_Pred, y_test))
print(classification_report(y_test,SVM_Pred,zero_division=0))

# Building the KNN
knn = KNeighborsClassifier(n_neighbors= 1)
# Training KNN
knn.fit(x_train,y_train)
# Testing KNN
knn_res = knn.predict(x_test)
# Getting the Testing results
comp = knn_res == y_test

true_R = 0
false_R = 0

for r in comp:
    if r:
        true_R += 1
    elif not r:
        false_R += 1
R_acc = (true_R/len(y_test)) * 100
# Printing results
print("\nK-Nearest neighbors accuracy is: ", false_R, " False predictions and ", true_R, " True Predictions, with accuracy of ", R_acc)
print("Confusion Matrix KNN: ")
print(confusion_matrix(knn_res, y_test))
print(classification_report(y_test, knn_res, zero_division= 0))

# Plotting the Histogram of the data
plt.hist(data['outcome'], color='blue', edgecolor='black', bins=50, label="Outcome data")
plt.show()


# print(data.dtypes)
# classes in the output
print('\n')
print('Total data:\n', data['outcome'].value_counts(), "\n")
print('Testing data are:\n', y_test.value_counts())
print('1- Discharge, 2- Death, 3- Stable, 4- Severe')

# Printing the Correlation between features
corr_mat = data.corr()
corr_mat.to_csv('correlation of variables.csv', index= False)
