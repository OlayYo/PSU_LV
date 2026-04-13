import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report # type: ignore
from sklearn.datasets import load_iris # type: ignore
from sklearn.tree import DecisionTreeClassifier, plot_tree # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore


df = pd.read_csv('C:/Users/student/Downloads/LV5-20260413/occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

skaler = StandardScaler()
X_train_s = skaler.fit_transform(X_train)
X_test_s = skaler.transform(X_test)

logreg = LogisticRegression()
logreg.fit(X_train_s, y_train)

y_pred = logreg.predict(X_test_s)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title('Logisticka regresija - Matrica zabune')
plt.show()

print("Tocnost:", round(accuracy_score(y_test, y_pred), 4))
print(classification_report(y_test, y_pred, target_names=class_names))

# Točnost 90.1%, najlošija od sve tri. Razlog je što granica između klasa nije linearna.
# Logistička regresija pretpostavlja linearnu granicu, a KNN i stablo mogu pratiti nelinearnu. To se vidi i na scatter plotu
