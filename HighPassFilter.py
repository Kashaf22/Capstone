import numpy as np
from scipy.signal import butter, filtfilt
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs  # Nyquist Frequency
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a
def highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y
# Example parameters
cutoff = 0.5  # Cutoff frequency in Hz
fs = 30  # Sampling rate in Hz
order = 6  # Order of the filter
# Your accelerometer data
# Replace 'your_data_here' with your actual data array
data = your_data_here  # This should be a NumPy array
filtered_data = highpass_filter(data, cutoff, fs, order)
# `filtered_data` is now the high-pass filtered version of the original data


