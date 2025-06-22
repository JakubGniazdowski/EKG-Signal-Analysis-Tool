# EKG Signal Analysis Tool 📈

A comprehensive Python tool for analyzing ECG (Electrocardiogram) signals using digital signal processing techniques.

## 🔬 Features

- **Raw ECG Signal Processing**: Load and analyze raw ECG data from multiple electrodes
- **Einthoven's Triangle Analysis**: Calculate standard ECG leads (I, II, III)
- **Signal Filtering**: High-pass filtering to remove baseline drift
- **Frequency Domain Analysis**: Power spectral density estimation using periodograms
- **Visualization**: Professional-grade plots with customizable styling

## 📊 Signal Processing Pipeline

1. **Data Loading**: Read raw ECG data from binary files
2. **Signal Extraction**: Separate signals from different electrodes (left arm, right arm, leg)
3. **Lead Calculation**: Compute Einthoven leads using differential amplification
4. **Filtering**: Apply high-pass filter (>1 Hz) to remove baseline wandering
5. **Analysis**: Generate time-domain and frequency-domain visualizations

## 🚀 Quick Start

### Prerequisites

```bash
pip install numpy matplotlib scipy
```

### Usage

```python
python analiza_EKG_zajecia.py
```

### Input Files

- `sig_128_calm.raw` - Raw ECG signal data (128 Hz sampling rate)
- `sig_128_calm.xml` - Signal metadata (optional)

### Output Files

- `daneEKG2.txt` - Filtered Einthoven leads data
- Multiple matplotlib figures showing signal analysis

## 📁 Project Structure

```
PIAB/
├── analiza_EKG_zajecia.py    # Main analysis script
├── sig_128_calm.raw          # Raw ECG data
├── sig_128_calm.xml          # Signal metadata
├── daneEKG2.txt             # Processed output data
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🔧 Technical Details

### Signal Parameters
- **Sampling Rate**: 128 Hz
- **Channels**: 5 (Ground, Left Arm, Right Arm, Sawtooth 1, Sawtooth 2)
- **Filter**: FIR High-pass filter with 1 Hz cutoff frequency

### Einthoven's Leads
- **Lead I**: LA - RA (Left Arm - Right Arm)
- **Lead II**: LL - RA (Left Leg - Right Arm)  
- **Lead III**: LL - LA (Left Leg - Left Arm)

### Generated Visualizations

1. **Figure 1**: Raw electrode signals (5 subplots)
2. **Figure 2**: Power spectral density of electrode signals
3. **Figure 3**: Einthoven leads (unfiltered)
4. **Figure 4**: Frequency spectra of Einthoven leads
5. **Figure 5**: High-pass filter frequency response
6. **Figure 6**: Filtered Einthoven leads

## 📈 Signal Analysis Features

### Time Domain Analysis
- Signal amplitude measurements
- Baseline drift visualization
- R-peak detection capabilities

### Frequency Domain Analysis
- Power spectral density estimation
- Frequency component identification
- Filter design and verification

## 🎨 Visualization Features

- Professional color schemes
- Grid overlays for better readability
- Consistent styling across all plots
- High-resolution output suitable for publications

## 🔬 Medical Applications

This tool is designed for:
- **Research**: ECG signal processing algorithm development
- **Education**: Teaching digital signal processing in biomedical applications
- **Analysis**: Baseline drift removal and noise filtering

## ⚠️ Important Notes

- This tool is for **research and educational purposes only**
- Not intended for clinical diagnosis
- Always consult medical professionals for ECG interpretation

## 🛠️ Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | ≥1.20.0 | Numerical computations |
| matplotlib | ≥3.5.0 | Data visualization |
| scipy | ≥1.7.0 | Signal processing |
## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

*Made with ❤️ for the biomedical signal processing community*

### 🪟 **Windows**

#### 1. Sprawdź wersję Python
```cmd
python --version
# lub
py --version
```

#### 2. Zainstaluj zależności
```cmd
REM Opcja A: Używając pip
pip install numpy matplotlib scipy

REM Opcja B: Używając pliku requirements.txt
pip install -r requirements.txt

REM Opcja C: Anaconda (zalecane)
conda install numpy matplotlib scipy
```

#### 3. Kompilacja (sprawdzenie składni)
```cmd
python -m py_compile analiza_EKG_zajecia.py
```

#### 4. Uruchomienie
```cmd
python analiza_EKG_zajecia.py
```

## Pliki wejściowe

Program wymaga następujących plików w tym samym katalogu:

- `sig_128_calm.raw` - dane sygnału EKG (format binarny)
- `sig_128_calm.xml` - metadane sygnału (opcjonalne)

### Pliki wyjściowe:
- `daneEKG2.txt` - przetworzone dane EKG (3 odprowadzenia Eindhovena)

## Rozwiązywanie problemów


### Problem: Błąd czcionki
```
findfont: Font family 'arial' not found
```
**Rozwiązanie**: To ostrzeżenie można zignorować - program użyje domyślnej czcionki.

### Problem: Nie wyświetlają się wykresy
**Linux**: Zainstaluj backend GUI:
```bash
sudo apt install python3-tk
```

**Windows**: Sprawdź czy masz zainstalowane:
```cmd
pip install matplotlib[qt]
```


## Autor
Jakub Gniazdowski
