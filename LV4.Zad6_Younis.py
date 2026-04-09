import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error

df = pd.read_csv('C:/Users/student/Desktop/projekt/web-labosi/LV2/public/images/LV4-20260409/cars_processed.csv')
df = df.drop(['name', 'mileage'], axis=1)

df = pd.get_dummies(df, columns=['fuel', 'seller_type', 'transmission', 'owner'])

X = df.drop('selling_price', axis=1)
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=300)

skaler = StandardScaler()
X_train_s = skaler.fit_transform(X_train)
X_test_s = skaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_s, y_train)

y_pred_train = model.predict(X_train_s)
y_pred_test = model.predict(X_test_s)

print("=== Rezultati na trening skupu (s kategorickim varijablama) ===")
print("R2:", round(r2_score(y_train, y_pred_train), 4))
print("MSE:", round(mean_squared_error(y_train, y_pred_train), 4))
print("MAE:", round(mean_absolute_error(y_train, y_pred_train), 4))

print("\n=== Rezultati na testnom skupu (s kategorickim varijablama) ===")
print("R2:", round(r2_score(y_test, y_pred_test), 4))
print("MSE:", round(mean_squared_error(y_test, y_pred_test), 4))
print("MAE:", round(mean_absolute_error(y_test, y_pred_test), 4))
print("Max error:", round(max_error(y_test, y_pred_test), 4))

plt.figure()
plt.scatter(y_pred_test, y_test, alpha=0.4)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'g-', linewidth=2)
plt.xlabel('Predikcija')
plt.ylabel('Stvarna vrijednost')
plt.title('Rezultati na testnim podacima (s kategorickim varijablama)')
plt.show()

