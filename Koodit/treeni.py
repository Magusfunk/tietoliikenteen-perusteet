from platform import java_ver
import numpy as np
import matplotlib.pyplot as plt


taajuustaso = np.zeros(100,dtype=complex)
taajuustaso[3] = complex(10,10)
taajuustaso[15] = complex(1,1)


aikataso = np.fft.fft(taajuustaso)

plt.figure(1,figsize=(14,7))
plt.subplot(211),plt.stem(aikataso.real),plt.title("Reeali osa")
plt.subplot(212),plt.stem(aikataso.imag),plt.title("Imag osa")
plt.subplots_adjust(hspace=0.8,top=0.95)
plt.show()