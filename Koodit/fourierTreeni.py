import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
s1 = np.cos(2*np.pi*5*t + (np.pi/4)) 
N = len(t)

taajuusTaso = (np.fft.fft(s1))/N
taajuusTasoPositiivinen = taajuusTaso[0:(int(N/2)+1)]
print(taajuusTaso.imag[5])

plt.figure(1)
plt.subplot(221),plt.plot(t,s1),plt.title("Aikatason signaali")
plt.subplot(222),plt.plot(taajuusTaso),plt.title("Taajuus tason signaali")
plt.subplot(223),plt.plot(np.abs(taajuusTaso)),plt.title("Taajuus tason signaali")
plt.subplot(224),plt.plot(np.hstack((taajuusTaso[980:1000],taajuusTaso[1:20])))
plt.show()