
import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('AD.csv', delimiter=',', skip_header=1)
# Assume 'data' is a 2D array containing the provided data
time_values = data[:, 0]  # Extract time values from the first column

# Calculate the sampling rate
time_diff = np.diff(time_values)
fs = 1 / np.mean(time_diff)

# Number of samples
num_samples = data.shape[0]

# Apply FFT to each dimension (x, y, z)
fft_x = np.fft.fft(data[:, 1])
fft_y = np.fft.fft(data[:, 2])
fft_z = np.fft.fft(data[:, 3])

# Compute the frequency spectrum magnitude
freq_spectrum_x = np.abs(fft_x)
freq_spectrum_y = np.abs(fft_y)
freq_spectrum_z = np.abs(fft_z)

# Calculate the frequency resolution
freq_resolution = fs / num_samples

# Create the frequency x-axis
frequencies = np.arange(0, num_samples // 2) * freq_resolution

# Create subplots for each dimension
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Plot the frequency spectrum for x-dimension
ax1.plot(frequencies, freq_spectrum_x[:num_samples // 2])
ax1.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Magnitude')
ax1.set_title('Frequency Spectrum - X Dimension')
ax1.grid(True)

# Plot the frequency spectrum for y-dimension
ax2.plot(frequencies, freq_spectrum_y[:num_samples // 2])
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude')
ax2.set_title('Frequency Spectrum - Y Dimension')
ax2.grid(True)

# Plot the frequency spectrum for z-dimension
ax3.plot(frequencies, freq_spectrum_z[:num_samples // 2])
ax3.set_xlabel('Frequency (Hz)')
ax3.set_ylabel('Magnitude')
ax3.set_title('Frequency Spectrum - Z Dimension')
ax3.grid(True)

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()