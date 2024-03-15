import numpy as np
from scipy.signal import butter, filtfilt
from numpy import fft
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt

def Mask(filteredData):
    magnitude_threshold = .5  # Adjust this value based on your requirements
    above_threshold_mask = np.abs(filteredData) > magnitude_threshold
    above_zero_mask = filteredData > 0
    final_mask = above_threshold_mask & above_zero_mask
    return filteredData * final_mask

data = np.genfromtxt('AD1.csv', delimiter=',', skip_header=1)

# Extract the time and x, y, z acceleration data from the array
time = data[:, 0]
acc_x = data[:, 1]
acc_y = data[:, 2]
acc_z = data[:, 3]

lowcut_freq = 3  # Lower cutoff frequency (Hz)
highcut_freq = 400.0  # Higher cutoff frequency (Hz)
sample_rate = 833  # Sample rate (Hz)
order = 2 # Filter order

nyquist_freq = 0.5 * sample_rate
low = lowcut_freq / nyquist_freq
high = highcut_freq / nyquist_freq
filtered_acc_x = Mask(sosfilt(butter(order, [low, high], btype='band', analog=False, output='sos'), acc_x))
filtered_acc_y = Mask(sosfilt(butter(order, [low, high], btype='band', analog=False, output='sos'), acc_y))
filtered_acc_z = Mask(sosfilt(butter(order, [low, high], btype='band', analog=False, output='sos'), acc_z))

# Plot the filtered data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
ax1.plot((time-time[0]), filtered_acc_y, linewidth=1.0)
ax1.set_title('Filtered Acceleration Data')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Acceleration (g)')

ax2.plot((time-time[0]), acc_y, linewidth=1.0)
ax2.set_title('Original Acceleration Data')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Acceleration (g)')
plt.show()