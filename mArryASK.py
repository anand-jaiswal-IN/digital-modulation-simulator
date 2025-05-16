import numpy as np
import matplotlib.pyplot as plt


def generate_message_signal(bits, Tb, fs):
    """
    Create a rectangular pulse train for input bits.
    bits: array of 0/1
    Tb: bit duration (s)
    fs: sampling rate (samples/s)
    """
    samples_per_bit = int(fs * Tb)
    # Each bit → samples_per_bit of amplitude = bit
    return np.repeat(bits, samples_per_bit)


def generate_carrier_signal(fc, duration, fs):
    """
    Generate a cosine carrier.
    fc: carrier frequency (Hz)
    duration: total time (s)
    fs: sampling rate (samples/s)
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    carrier = np.cos(2 * np.pi * fc * t)
    return t, carrier


def bits_to_symbols(bits, M):
    """
    Group bits into symbol indices (0..M-1).
    Pads with zeros if len(bits)%k != 0.
    """
    k = int(np.log2(M))
    if len(bits) % k != 0:
        bits = np.hstack([bits, np.zeros(k - len(bits) % k, dtype=int)])
    symbols = []
    for i in range(0, len(bits), k):
        # Convert k-bit chunk to integer
        chunk = bits[i : i + k]
        val = int("".join(chunk.astype(str)), 2)
        symbols.append(val)
    return np.array(symbols)


def m_ask_modulation(symbols, M, fc, fs, Ts):
    """
    Perform M-ASK modulation.
    symbols: array of indices 0..M-1
    Ts: symbol duration (s)
    """
    # Amplitude levels centered at zero
    levels = 2 * np.arange(M) - (M - 1)
    samples_per_sym = int(fs * Ts)
    t_sym = np.linspace(0, Ts, samples_per_sym, endpoint=False)

    signal = np.array([])
    for sym in symbols:
        A = levels[sym]
        # Modulate carrier for this symbol
        sig = A * np.cos(2 * np.pi * fc * t_sym)
        signal = np.concatenate([signal, sig])
    # Full time vector
    t = np.linspace(
        0, Ts * len(symbols), samples_per_sym * len(symbols), endpoint=False
    )
    return t, signal


if __name__ == "__main__":
    # === Parameters ===
    M = 8  # M-ary level :contentReference[oaicite:6]{index=6}
    bit_rate = 4  # bits per second
    fs = 1000  # sampling freq (samples/sec)
    fc = 20  # carrier freq (Hz)
    num_bits = 24  # total bits

    Tb = 1 / bit_rate  # bit duration
    k = int(np.log2(M))  # bits per symbol
    Ts = k * Tb  # symbol duration

    # === Generate message and carrier ===
    bits = np.random.randint(
        0, 2, num_bits
    )  # random bits :contentReference[oaicite:7]{index=7}
    msg = generate_message_signal(bits, Tb, fs)  # rectangular message pulses
    t_msg = np.linspace(0, Tb * num_bits, len(msg), endpoint=False)

    t_car, carrier = generate_carrier_signal(fc, Tb * num_bits, fs)

    # === M-ASK modulation ===
    symbols = bits_to_symbols(
        bits, M
    )  # symbol mapping :contentReference[oaicite:8]{index=8}
    t_ask, ask_sig = m_ask_modulation(symbols, M, fc, fs, Ts)

    # === Plotting ===
    plt.figure(figsize=(12, 8))

    # Message signal
    plt.subplot(3, 1, 1)
    plt.plot(t_msg, msg, "k")
    plt.title("Message Signal (Rectangular Pulses)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # Carrier signal
    plt.subplot(3, 1, 2)
    plt.plot(t_car, carrier, "m")
    plt.title(f"Carrier Signal (f_c = {fc} Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # M-ASK signal
    plt.subplot(3, 1, 3)
    plt.plot(t_ask, ask_sig, "C3")
    plt.title(f"{M}-ary ASK Modulated Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude Levels")
    plt.grid(True)

    plt.tight_layout()

    # === Save to file ===
    plt.savefig("m-array-ask.png")
