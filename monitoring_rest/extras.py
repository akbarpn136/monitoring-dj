import numpy
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


class DoFFT(object):
    def __init__(self, data, sampel_spacing, first_cutoff, second_cutoff, order):
        self.data = data
        self.sample_spacing = sampel_spacing
        self.first_cutoff = first_cutoff
        self.second_cutoff = second_cutoff
        self.order = order
        super(DoFFT, self).__init__()

    def make_fft(self):
        # Data akselerometer
        numpy_data_acc = numpy.array(self.data).flatten()

        # Jumlah data
        N = numpy_data_acc.size

        # Sample spacing
        T = self.sample_spacing

        if N > 0:
            # FFT
            fltr = DoFilter(data=numpy_data_acc).butter_bandpass_filter(self.first_cutoff,
                                                                        self.second_cutoff,
                                                                        1 / T,
                                                                        order=self.order)
            zf = numpy.fft.fft(fltr)
            m = numpy.absolute(zf[:N // 2])
            yf = numpy.fft.fftfreq(N, d=T).tolist()

            y = yf[:N // 2]
            z = m.tolist()

        else:
            y = numpy.zeros(N//2).tolist()
            z = numpy.zeros(N//2).tolist()

        return N, y, z
