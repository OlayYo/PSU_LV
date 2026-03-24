import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('C:/Users/student/Pictures/LV3-20260324/mtcars.csv')

srednja_potrosnja = mtcars.groupby('cyl')['mpg'].mean()
plt.figure()
plt.bar(['4 cil', '6 cil', '8 cil'], srednja_potrosnja.values, color='red')
plt.title('Srednja potrosnja po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('mpg')
plt.show()

grupe_tezina = [mtcars[mtcars.cyl == c]['wt'].values for c in [4, 6, 8]]
plt.figure()
plt.boxplot(grupe_tezina, tick_labels=['4 cil', '6 cil', '8 cil'])
plt.title('Distribucija tezine po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('wt (lb/1000)')
plt.show()

automatski = mtcars[mtcars.am == 0]['mpg'].values
rucni = mtcars[mtcars.am == 1]['mpg'].values
plt.figure()
plt.boxplot([automatski, rucni], tick_labels=['Automatski', 'Rucni'])
plt.title('Potrosnja (rucni vs automatski mjenjac)')
plt.ylabel('mpg')
plt.show()

auto = mtcars[mtcars.am == 0]
rucnim = mtcars[mtcars.am == 1]
plt.figure()
plt.scatter(auto.hp, auto.qsec, color='green', label='Automatski', alpha=0.7)
plt.scatter(rucnim.hp, rucnim.qsec, color='blue', label='Rucni', alpha=0.7)
plt.title('Ubrzanje vs snaga po tipu mjenjaca')
plt.xlabel('hp')
plt.ylabel('qsec (1/4 milje)')
plt.legend()
plt.show()

