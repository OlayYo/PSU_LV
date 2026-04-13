import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report # type: ignore
from sklearn.datasets import load_iris # type: ignore
from sklearn.tree import DecisionTreeClassifier, plot_tree # type: ignore

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

clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_train_s, y_train)

y_pred = clf.predict(X_test_s)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title('Stablo odlucivanja - Matrica zabune')
plt.show()

print("Tocnost:", round(accuracy_score(y_test, y_pred), 4))
print(classification_report(y_test, y_pred, target_names=class_names))

plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=feature_names, class_names=class_names, filled=True)
plt.title('Stablo odlucivanja')
plt.show()

# Točnost 94.1%, malo lošije od KNN. max_depth=5. Ako ga povećaš model se prefituje, ako smanjiš gubi na točnosti. 
# Skaliranje ne utječe previše na stablo jer ono ne koristi udaljenosti.
