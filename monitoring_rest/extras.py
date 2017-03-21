from scipy import signal as sig


class DoFilter(object):
    def __init__(self, data):
        self.data = data
        super(DoFilter, self).__init__()

    def butter_bandpass_filter(self, lowcut, highcut, fs, order=3):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq

        a = sig.butter(N=order, Wn=[low, high], btype='bandpass')
        y = sig.lfilter(a[0], a[1], self.data)

        return y
