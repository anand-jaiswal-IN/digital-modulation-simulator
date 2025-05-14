import numpy as np
import matplotlib.pyplot as plt

import signal_generation, modulations


# Parameters
bit_rate = input("Enter the bit rate (bits/sec) [default: 1]: ")  # bits per second
bit_rate = 1 if bit_rate == "" else int(bit_rate)

bit_duration = 1 / bit_rate

fc = input("Enter the carrier frequency (Hz) [default: 5]: ")  # carrier frequency (Hz)
fc = 5 if fc == "" else int(fc)

fs = input(
    "Enter the sampling frequency (samples/sec) [default: 1000]: "
)  # sampling frequency (samples/sec)
fs = 1000 if fs == "" else int(fs)

num_bits = input(
    "Enter the number of bits to transmit [default: 8]: "
)  # number of bits to transmit
num_bits = 8 if num_bits == "" else int(num_bits)

t_bit = np.linspace(0, bit_duration, int(fs * bit_duration), endpoint=False)


# Generate random bitstream
bits = np.random.randint(0, 2, num_bits)
print("Transmitted Bits:", bits)


# === Generate signals ===

# Time vector for the full message
t_full = np.linspace(0, bit_duration * num_bits, num_bits * len(t_bit), endpoint=False)

message_signal = signal_generation.generate_message_signal(bits, t_bit)
carrier_time, carrier_signal = signal_generation.generate_carrier_signal(
    fc, bit_duration * num_bits, fs
)

ask_signal = modulations.ask_modulation(bits, t_bit, fc)
fsk_signal = modulations.fsk_modulation(bits, t_bit, fc)
psk_signal = modulations.psk_modulation(bits, t_bit, fc)


# === Plotting ===
plt.figure(figsize=(15, 10))

plt.subplot(5, 1, 1)
plt.title("Message Signal")
plt.plot(t_full, message_signal, "k")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 2)
plt.title("Carrier Signal")
plt.plot(carrier_time, carrier_signal, "m")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 3)
plt.title("ASK Modulated Signal")
plt.plot(t_full, ask_signal, "b")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 4)
plt.title("FSK Modulated Signal")
plt.plot(t_full, fsk_signal, "g")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(5, 1, 5)
plt.title("PSK Modulated Signal")
plt.plot(t_full, psk_signal, "r")
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.grid(True)

plt.tight_layout()

plt.savefig("modulated_signal.png")
print("Plot saved as modulation_output.png")
