import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/student/Downloads/LV5-20260413/occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

print("b) Broj podatkovnih primjera:", len(df))
print("c) Razdioba po klasama:")
print(df[target_name].value_counts())

plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()

# 10129 primjera, od toga 8228 slobodnih i 1901 zauzetih. Na scatter plotu se vidi da zauzeta prostorija ima veće CO2 vrijednosti.