import numpy as np


def generate_message_signal(bits, t_bit):
    """Return time vector and binary message signal"""
    message = np.array([])
    for bit in bits:
        message = np.concatenate((message, np.ones_like(t_bit) * bit))
    return message


def generate_carrier_signal(freq, total_time, fs):
    """Return a cosine carrier signal"""
    t = np.linspace(0, total_time, int(fs * total_time), endpoint=False)
    return t, np.cos(2 * np.pi * freq * t)
