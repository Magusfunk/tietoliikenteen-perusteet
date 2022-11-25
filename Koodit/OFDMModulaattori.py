import numpy as np
import matplotlib.pyplot as plt

taajuustaso = np.zeros((128),dtype=complex)
taajuustaso[3] = complex(2,2);  # Tässä on nyt moduloitu yksi alikantoaalto
taajuustaso[10] = complex(1,1);  # Tässä on nyt moduloitu yksi alikantoaalto
taajuustaso[30] = complex(1,-1);  # Tässä on nyt moduloitu yksi alikantoaalto
taajuustaso[40] = complex(-1,-1);  # Tässä on nyt moduloitu yksi alikantoaalto
taajuustaso[50] = complex(-1,1);  # Tässä on nyt moduloitu yksi alikantoaalto
# Moduloi tähän myös alikantoaallot 10 ja 30 QPSK-modulaatiota käyttäen
# Eli tarkoittaa siis sitä, että sinulla on käytettävissäsi 
# 00 => 1+j, 
# 11 => -1-j, 
# 01 => -1+j ja 
# 10 => 1-j vaihtoehdot.

# print(taajuustaso[:])

aikataso = np.fft.ifft(taajuustaso[:])
# print(aikataso.real)
# print(aikataso.imag)

taajustasoPalautus = np.fft.fft(aikataso)
print(taajustasoPalautus[10])

for x in enumerate(taajustasoPalautus):
    if x[1] == complex(1,1): 
        print("Bittipäätös kanavassa",x[0],"on: 00")        
    if x[1] == complex(-1,1): 
        print("Bittipäätös kanavassa",x[0],"on: 01")  
    if x[1] == complex(1,-1): 
        print("Bittipäätös kanavassa",x[0],"on: 10")  
    if x[1] == complex(-1,-1): 
        print("Bittipäätös kanavassa",x[0],"on: 11")    

plt.figure(1)
plt.subplot(311)
plt.plot(aikataso.real)
plt.title('Moduloidun signaalin kosinihaara')
plt.subplot(312)
plt.plot(aikataso.imag)
plt.title('Moduloidun signaalin sinihaara')
plt.show()

# Ja tänne pitäisi opiskelijan sitten osata tehdä bittipäätökset
# Eli sinun pitää tulla aikatason signaalista takaisin taajuustasoon
# ja tehdä bittipäätökset alikantoaaltojen 3, 10, 30 osalta.

# for x in np.nditer(taajustasoPalautus):
#     if x == complex(1,1):
#         bitti = "00"
#         print("Bittipäätös on =", bitti)
#     elif x == complex(-1,1):
#         bitti = "01"
#         print("Bittipäätös on =", bitti)
#     elif x == complex(1,-1):
#         bitti = "00"
#         print("Bittipäätös on =", bitti)
#     elif x == complex(-1,-1):
#         bitti = "11"
#         print("Bittipäätös on =", bitti)
#     else:
#         continue