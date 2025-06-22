# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-06-22

### Added ✨
- Initial release of EKG Signal Analysis Tool
- Raw ECG signal loading from binary files (.raw format)
- Einthoven's triangle lead calculations (I, II, III)
- High-pass filtering (>1 Hz) for baseline drift removal
- Power spectral density analysis using periodograms
- Professional visualization with matplotlib
- Multi-channel electrode signal processing
- FIR filter design and frequency response analysis
- Export functionality for processed signals

### Features 🔧
- **Signal Processing Pipeline**
  - 128 Hz sampling rate support
  - 5-channel electrode configuration
  - Differential amplification for lead calculation
  - Zero-phase filtering using filtfilt

- **Visualization Suite**
  - Time-domain signal plots
  - Frequency-domain spectral analysis
  - Filter characteristic visualization
  - Professional color schemes and styling

- **Data Export**
  - Filtered Einthoven leads output to text file
  - Compatible with further analysis tools

### Technical Specifications 📊
- **Input Format**: Float32 binary data
- **Sampling Rate**: 128 Hz
- **Filter Type**: FIR High-pass (501 taps)
- **Cutoff Frequency**: 1 Hz
- **Output Format**: ASCII text file

### Dependencies 📦
- numpy >= 1.20.0
- matplotlib >= 3.5.0  
- scipy >= 1.7.0

