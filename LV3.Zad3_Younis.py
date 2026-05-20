import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'

airQualityHR = urllib.request.urlopen(url).read()
root = ET.fromstring(airQualityHR)

df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

children = list(root)
i = 0
while True:
    try:
        obj = list(children[i])
    except:
        break
    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = pd.concat([df, row_s.to_frame().T], ignore_index=True)
    df.at[i, 'mjerenje'] = float(df.mjerenje[i])
    i = i + 1

df.vrijeme = pd.to_datetime(df.vrijeme, utc=True)
df.mjerenje = df.mjerenje.astype(float)

df.plot(y='mjerenje', x='vrijeme', title='PM10 - Osijek 2017')
plt.ylabel('PM10 (ug/m3)')
plt.show()

print("Tri datuma s najvecom koncentracijom PM10 u Osijeku 2017:")
print(df.sort_values('mjerenje', ascending=False).head(3)[['vrijeme', 'mjerenje']])
