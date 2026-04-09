import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('C:/Users/student/Desktop/projekt/web-labosi/LV2/public/images/LV4-20260409/cars_processed.csv')
print("1. Broj automobila u datasetu: ", len(df))
print()
print("2. Tip stupaca: ")
print(df.dtypes)
print()
print("3. Automobil s najvecom cijenom: ", df.loc[df.selling_price.idxmax(), 'name'])
print("Automobil s najmanjom cijenom:", df.loc[df.selling_price.idxmin(), 'name'])
print()
print("4. Broj automobila proizvodenih 2012.: ", len(df[df.year == 2012]))
print()
print("5. Automobil s najvise km: ", df.loc[df.km_driven.idxmax(), 'name'], "-", df.km_driven.max(), "km")
print("Automobil s najmanje km: ", df.loc[df.km_driven.idxmin(), 'name'], "-", df.km_driven.min(), "km")
print()
print("6. Najcesci broj sjedala: ", df.seats.mode()[0])
print()
print("7. Prosjecna kilometraza (dizel motor): ", round(df[df.fuel == 'Diesel'].km_driven.mean(), 2))
print("Prosjecna kilometraza (benzin motor): ", round(df[df.fuel == 'Petrol'].km_driven.mean(), 2))

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by='fuel', column=['selling_price'], grid=False)
df.hist(['selling_price'], grid=False)

plt.show()