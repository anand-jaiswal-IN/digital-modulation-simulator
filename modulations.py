import numpy as np


def ask_modulation(bits, t_bit, fc):
    ask_signal = np.array([])
    for bit in bits:
        carrier = np.cos(2 * np.pi * fc * t_bit)
        ask_signal = np.concatenate((ask_signal, bit * carrier))
    return ask_signal


def fsk_modulation(bits, t_bit, fc):
    f1 = fc - 2
    f2 = fc + 2
    fsk_signal = np.array([])
    for bit in bits:
        freq = f1 if bit == 0 else f2
        fsk_signal = np.concatenate((fsk_signal, np.cos(2 * np.pi * freq * t_bit)))
    return fsk_signal


def psk_modulation(bits, t_bit, fc):
    psk_signal = np.array([])
    for bit in bits:
        phase = 0 if bit == 0 else np.pi
        psk_signal = np.concatenate(
            (psk_signal, np.cos(2 * np.pi * fc * t_bit + phase))
        )
    return psk_signal
