import random
from scipy.signal import butter, lfilter, filtfilt


# fs : Sample rate

def gen_hex_colour_code():
    return ''.join([random.choice('123456789ABCDEF') for x in range(5)])


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')

    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    # y = lfilter(b, a, data)
    y = filtfilt(b, a, data)
    return y
