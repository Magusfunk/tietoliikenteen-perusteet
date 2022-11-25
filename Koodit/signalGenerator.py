import viikko1tehtävä3
from viikko1tehtävä3 import signalAnalyser as SA


t = int(input("Anna aika 1-10 sekunttia: "))
print("Aika = ",t,"s")
f = int(input("Anna taajuus 0-500: "))
print("Taajuus = ", f,"Hz")
fs= int(input("Anna näytteenottoepisteiden määrä: "))
print("Pisteet = ", fs)

objekti = SA(fs,t)
objekti.create(f)
objekti.plot(0,fs)