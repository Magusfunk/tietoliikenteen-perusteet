import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" 
Tehtävä 1: 
- lataa Latest https://covidtracking.com/data/download/national-history.csv
  tiedosto pandas kirjaston avulla Pandas dataframeksi. 
- "Irroita" siitä ladattaessa'date','deaths','hospitalInc','hospitalNow' sarakkeet
- Piirrä matplotlib.pyplot kirjaston ja plt.subplot, plt.plot, plt.title, plt.show 
  komentojen avulla kuva, josta nähdään kuolleiden lukumäärät, sairaalapotilaiden
  inkrementaalinen kasvu ja kuinka paljon sairaalassa on potilaita eri päivinä.
- Selvitä minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä

Tehtävä 2:
- Muuta kaikki dataFramen sarakkeet numpy arrayksi to_numpy() funktion avulla
- Tulosta kuolleiden määrä ja sairaalassa olleiden lukumäärät oikeassa järjestyksessä
  (huom päivämäärät ovat tiedostossa viimeisin päivämäärä ensin. Eli käännä tulostusjärjestys
   siten, että kuvaan tulostetaan deaths sarakkeen viimeisin alkio ensin jne.)
""" 

df = pd.read_csv("national-history.csv",
                  usecols=["death","hospitalizedIncrease","hospitalizedCurrently"])
df = df.dropna(axis=0)
xAxis = np.arange(0,len(df.index))
sizeX = 8
sizeY = 12


plt.figure(1,figsize=(sizeX, sizeY))
plt.subplot(311)
plt.title("Deaths")
plt.plot(xAxis,df["death"])
plt.subplot(312)
plt.title("Hospitalized Increased")
plt.plot(xAxis,df["hospitalizedIncrease"])
plt.subplot(313)
plt.title("Hospitalized Currently")
plt.plot(xAxis,df["hospitalizedCurrently"])

df = df.loc[::-1]
plt.figure(2,figsize=(sizeX, sizeY))
plt.subplot(311)
plt.title("Deaths")
plt.plot(xAxis,df["death"])
plt.subplot(312)
plt.title("Hospitalized Increased")
plt.plot(xAxis,df["hospitalizedIncrease"])
plt.subplot(313)
plt.title("Hospitalized Currently")
plt.plot(xAxis,df["hospitalizedCurrently"])
plt.show()