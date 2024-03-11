import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
# Load the .csv file into a NumPy array, skipping the header row
data = np.genfromtxt('AD.csv', delimiter=',', skip_header=1)

# Extract the time and x, y, z acceleration data from the array
time = data[:, 0]
acc_x = data[:, 1]
acc_y = data[:, 2]
acc_z = data[:, 3]

# Define the highpass filter parameters
cutoff_freq = 10.0  # Cutoff frequency in Hz
sample_rate = 1.0 / (time[1] - time[0])  # Sample rate calculated from time difference
order = 10  # Filter order

# Calculate the filter coefficients
nyquist_freq = 0.5 * sample_rate
normalized_cutoff_freq = cutoff_freq / nyquist_freq
b, a = butter(order, normalized_cutoff_freq, btype='high', analog=False)

# Apply the highpass filter to each acceleration dimension
filtered_acc_x = filtfilt(b, a, acc_x)
filtered_acc_y = filtfilt(b, a, acc_y)
filtered_acc_z = filtfilt(b, a, acc_z)

# Calculate the magnitude of the filtered acceleration vectors
filtered_acc_mag = np.sqrt(filtered_acc_x**2 + filtered_acc_y**2 + filtered_acc_z**2)

# Find the index of the highest magnitude
max_index = np.argmax(filtered_acc_mag)

print(filtered_acc_x)
plt.style.use('_mpl-gallery')

# plot
fig, (ax,ax2) = plt.subplots(1,2,figsize=(10,6))

ax.plot((time-1846), filtered_acc_y, linewidth=1.0)
ax.set_title('Filtered Acceleration Data')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (g)')
ax2.plot((time-1846), acc_y, linewidth=1.0)
ax2.set_title('Original Acceleration Data')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Acceleration (g)')
plt.show()