import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *
from scipy.signal import periodogram, firwin, freqz, filtfilt
import os

plt.close('all')
sygnal = np.fromfile('sig_128_calm.raw', dtype=np.float32)
L = len(sygnal)
syg_matrix = np.reshape(sygnal, [L//5, 5])
Fp = 128.0
Tp = 1/Fp
t = np.arange(0, ((L//5))*Tp, Tp) 
rekaL = syg_matrix[:,1]
rekaP = syg_matrix[:,2]
noga = syg_matrix[:,0]
saw1 = syg_matrix[:,3]
saw2 = syg_matrix[:,4]

plt.figure(1, figsize=(14, 12))
plt.subplot(511)
plt.plot(t, noga, color='#1f77b4', linewidth=1.5)
plt.title('Elektroda nogi (Ground)', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.grid(True, alpha=0.3)

plt.subplot(512)
plt.plot(t, rekaL, color='#ff7f0e', linewidth=1.5)
plt.title('Elektroda ręki lewej', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.grid(True, alpha=0.3)

plt.subplot(513)
plt.plot(t, rekaP, color='#2ca02c', linewidth=1.5)
plt.title('Elektroda ręki prawej', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.grid(True, alpha=0.3)

plt.subplot(514)
plt.plot(t, saw1, color='#d62728', linewidth=1.5)
plt.title('Sygnał piłokształtny 1', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.grid(True, alpha=0.3)

plt.subplot(515)
plt.plot(t, saw2, color='#9467bd', linewidth=1.5)
plt.title('Sygnał piłokształtny 2', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.xlabel('Czas [s]', fontsize=12)
plt.grid(True, alpha=0.3)

plt.suptitle('Sygnały z elektrod - oryginalne', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.88)  

[f,WrekaL] = periodogram(rekaL, Fp) 
[f,WrekaP] = periodogram(rekaP, Fp)
[f,Wnoga] = periodogram(noga, Fp)

plt.figure(2, figsize=(12, 10))
plt.subplot(311)
plt.semilogy(f, WrekaL, color='#ff7f0e', linewidth=1.5)
plt.title('Widmo  - Ręka lewa', fontsize=14, pad=10)
plt.grid(True, alpha=0.3)
plt.xlim(0, 64)

plt.subplot(312)
plt.semilogy(f, WrekaP, color='#2ca02c', linewidth=1.5)
plt.title('Widmo  - Ręka prawa', fontsize=14, pad=10)
plt.grid(True, alpha=0.3)
plt.xlim(0, 64)

plt.subplot(313)
plt.semilogy(f, Wnoga, color='#1f77b4', linewidth=1.5)
plt.title('Widmo  - Noga (Ground)', fontsize=14, pad=10)
plt.xlabel('Częstotliwość [Hz]', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, 64)

plt.suptitle('Widma sygnałów z elektrod', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.88)  


odprI = rekaL - rekaP
odprII = noga - rekaP
odprIII = noga - rekaL

plt.figure(3, figsize=(14, 10))
plt.subplot(311)
plt.plot(t, odprI, color='#e74c3c', linewidth=1.5)
plt.title('Odprowadzenie I (Ręka lewa - Ręka prawa)', fontsize=12, pad=5)
plt.grid(True, alpha=0.3)

plt.subplot(312)
plt.plot(t, odprII, color='#8e44ad', linewidth=1.5)
plt.title('Odprowadzenie II (Noga - Ręka prawa)', fontsize=12, pad=5)
plt.grid(True, alpha=0.3)

plt.subplot(313)
plt.plot(t, odprIII, color='#f39c12', linewidth=1.5)
plt.title('Odprowadzenie III (Noga - Ręka lewa)', fontsize=12, pad=5)
plt.xlabel('Czas [s]', fontsize=12)
plt.grid(True, alpha=0.3)

plt.suptitle('Sygnały Eindhovena (niefiltrowane)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.88)  


[f,widmoI] = periodogram(odprI, Fp)
[f,widmoII] = periodogram(odprII, Fp)
[f,widmoIII] = periodogram(odprIII, Fp)

plt.figure(4, figsize=(12, 10))
plt.subplot(311)
plt.semilogy(f, widmoI, color='#e74c3c', linewidth=1.5)
plt.title('Widmo  - Odprowadzenie I (LA - RA)', fontsize=12, pad=5)
plt.grid(True, alpha=0.3)
plt.xlim(0, 25)

plt.subplot(312)
plt.semilogy(f, widmoII, color='#8e44ad', linewidth=1.5)
plt.title('Widmo  - Odprowadzenie II (LL - RA)', fontsize=12, pad=5)
plt.grid(True, alpha=0.3)
plt.xlim(0, 25)

plt.subplot(313)
plt.semilogy(f, widmoIII, color='#f39c12', linewidth=1.5)
plt.title('Widmo  - Odprowadzenie III (LL - LA)', fontsize=12, pad=5)
plt.xlabel('Częstotliwość [Hz]', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, 25)

plt.suptitle('Widma sygnałów Eindhovena', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.88)  



b = firwin(501, 1, pass_zero=False, fs=Fp)
w, h = freqz(b, 1, worN=8000, fs=Fp)


plt.figure(5, figsize=(10, 6))
plt.plot(w, 20 * np.log10(abs(h)), color='#2980b9', linewidth=2)
plt.title('Odpowiedź filtru górnoprzepustowego - Amplituda', fontsize=14, pad=10)
plt.xlabel('Częstotliwość [Hz]', fontsize=12)
plt.ylabel('Wzmocnienie [dB]', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(0, 10)
plt.ylim(-60, 5)
plt.axvline(1, color='red', linestyle='--', alpha=0.7, label='Częst. odcięcia: 1 Hz')
plt.legend()
plt.tight_layout()


odprIF = filtfilt(b, 1, odprI)
odprIIF = filtfilt(b, 1, odprII)
odprIIIF = filtfilt(b, 1, odprIII)


plt.figure(6, figsize=(14, 10))
plt.subplot(311)
plt.plot(t, odprIF, color='#e74c3c', linewidth=1.5)
plt.title('Odprowadzenie I - po filtracji HP (>1 Hz)', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.grid(True, alpha=0.3)

plt.subplot(312)
plt.plot(t, odprIIF, color='#8e44ad', linewidth=1.5)
plt.title('Odprowadzenie II - po filtracji HP (>1 Hz)', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.grid(True, alpha=0.3)

plt.subplot(313)
plt.plot(t, odprIIIF, color='#f39c12', linewidth=1.5)
plt.title('Odprowadzenie III - po filtracji HP (>1 Hz)', fontsize=12, pad=5)
plt.ylabel('Napięcie [μV]', fontsize=11)
plt.xlabel('Czas [s]', fontsize=12)
plt.grid(True, alpha=0.3)

plt.suptitle('Sygnały Eindhovena po filtracji górnoprzepustowej', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.subplots_adjust(top=0.88)  


macierz = np.zeros(shape=(L//5, 3))
macierz[:,0] = odprIF
macierz[:,1] = odprIIF
macierz[:,2] = odprIIIF

np.savetxt('daneEKG2.txt', macierz)


plt.show()


