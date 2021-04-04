import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from pandas import read_csv


# 1 Import dataset
dataset = read_csv("pendapatan.csv")

# 2. Memisahkan feature matrix (X) dengan target label (Y)
X = dataset.drop('Class', axis=1)
Y = dataset['Class']

# 3. Splitting
Xtrain, Xtest, ytrain, ytest = train_test_split(X, Y, random_state=0)

# 4. Training model
model = GaussianNB()
model.fit(Xtrain, ytrain)       # training model dengan method fit()

# 5. Melihat skor akurasi dengan data ytest menggunakan algortima naive bayes
y_model = model.predict(Xtest)
print(accuracy_score(ytest, y_model))
print(confusion_matrix(ytest, y_model))
print(classification_report(ytest, y_model))

# 6 save trained model
filename = "olah-data-predik.data"
with open(filename, 'wb') as file:
    pickle.dump(model, file)