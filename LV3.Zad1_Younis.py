import pandas as pd
import numpy as np

mtcars = pd.read_csv('C:/Users/student/Pictures/LV3-20260324/mtcars.csv')

print("\n1. Pet automobila s najvecom potrosnjom:")
print(mtcars.sort_values(by='mpg', ascending=False).head(5))

print("\n2. Automibili s 8 cilindra s najmanjom potrosnjom:")
print(mtcars[mtcars.cyl == 8].sort_values(by = 'mpg', ascending=True).head(3))

print("\n3. Srednja potrosnja automobila s 6 cilindra")
print(mtcars[mtcars.cyl == 6]['mpg'].mean())

print("\n4. Srednja potrosnja automobila s 4 cilindra mase izmedu 2000 i 2200 lbs:")
print(mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)]['mpg'].mean())

print("\n5. Broj automobila po tipu mjenjaca:")
print("Automatski:", len(mtcars[mtcars.am == 0]))
print("Rucni:", len(mtcars[mtcars.am == 1]))

print("\n6. Automobili s automatskim mjenjacom i snagom preko 100 hp:")
print(len(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)]))

print("\n7. Masa automobila:")
mtcars['wt_kg'] = mtcars.wt * 1000 * 0.453592
print(mtcars[['car', 'wt_kg']])
