# Code Documentation

## Module Overview

This module provides comprehensive ECG signal analysis capabilities including signal processing, filtering, and visualization.

## Main Functions and Classes

### Data Loading
```python
sygnal = np.fromfile('sig_128_calm.raw', dtype=np.float32)
```
Loads raw ECG data from binary file format.

### Signal Processing Pipeline

#### 1. Data Reshaping
```python
syg_matrix = np.reshape(sygnal, [L//5, 5])
```
Reshapes 1D signal array into 5-channel matrix:
- Channel 0: Ground electrode (leg)
- Channel 1: Left arm electrode  
- Channel 2: Right arm electrode
- Channel 3: Sawtooth signal 1
- Channel 4: Sawtooth signal 2

#### 2. Einthoven Lead Calculation
```python
odprI = rekaL - rekaP      # Lead I: LA - RA
odprII = noga - rekaP      # Lead II: LL - RA  
odprIII = noga - rekaL     # Lead III: LL - LA
```
Computes standard 12-lead ECG leads using Einthoven's triangle configuration.

#### 3. Filter Design
```python
b = firwin(501, 1, pass_zero=False, fs=Fp)
```
Creates FIR high-pass filter:
- **Order**: 501 taps
- **Cutoff**: 1 Hz
- **Type**: High-pass (removes baseline drift)
- **Method**: Windowed sinc function

#### 4. Signal Filtering
```python
odprIF = filtfilt(b, 1, odprI)
```
Applies zero-phase filtering to preserve signal characteristics.

### Visualization Functions

#### Time-Domain Plotting
```python
plt.plot(t, signal, color='#color', linewidth=1.5)
```
Generates professional time-domain visualizations with:
- Consistent color schemes
- Grid overlays for readability
- Proper axis labeling and units

#### Frequency-Domain Analysis  
```python
[f, spectrum] = periodogram(signal, Fp)
plt.semilogy(f, spectrum)
```
Creates power spectral density plots using Welch's periodogram method.

## Signal Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Sampling Rate | 128 Hz | Signal acquisition frequency |
| Filter Order | 501 | FIR filter length |
| Cutoff Frequency | 1 Hz | High-pass filter cutoff |
| Channels | 5 | Number of input channels |

## Mathematical Background

### Einthoven's Triangle
The standard ECG leads are calculated using the electrical potential differences between electrodes:

- **Lead I**: Potential difference between left arm and right arm
- **Lead II**: Potential difference between left leg and right arm  
- **Lead III**: Potential difference between left leg and left arm

### High-Pass Filtering
Baseline drift removal using FIR filter:
- Removes low-frequency components (< 1 Hz)
- Preserves ECG morphology
- Zero-phase implementation prevents signal distortion

### Power Spectral Density
Frequency analysis using periodogram:
- Identifies dominant frequency components
- Helps detect noise and artifacts
- Validates filter performance

## Error Handling

The code includes basic error handling for:
- File loading operations
- Matrix dimensionality checks
- Filter stability verification

## Performance Considerations

- **Memory Usage**: O(n) where n is signal length
- **Computational Complexity**: O(n log n) for FFT operations
- **Processing Time**: Typically < 1 second for standard ECG files

## Future Enhancements

Potential improvements:
- Real-time processing capabilities
- Advanced arrhythmia detection
- Multi-format file support
- Interactive visualization tools
