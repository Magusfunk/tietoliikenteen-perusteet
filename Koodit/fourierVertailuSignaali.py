import numpy as np
import matplotlib.pyplot as plt

N = 100
j = complex(0,1)
k = 0
n = np.arange(0,N,1)
v0 = np.exp((-j*2*np.pi*k*n)/N)
k = 90
v1 = np.exp((-j*2*np.pi*k*n)/N)

plt.figure(1,figsize=(20,8))
plt.subplot(611),plt.stem(v0),plt.title("Eka vertailusignaali")
plt.subplot(612),plt.stem(v1.real),plt.title("Toka cos vertailusignaali")
plt.subplot(613),plt.stem(v1.imag),plt.title("Toka sin vertailusignaali")
plt.subplots_adjust(hspace=0.8,top=0.95)
plt.show()