import pandas as pd
import mne
import sys
import numpy as np
from mne import Epochs, pick_types, find_events
from sklearn.pipeline import Pipeline
from mne.io import read_raw_edf



#https://physionet.org/content/eegmmidb/1.0.0/
#https://scikit-learn.org/stable/index.html
#https://mne.tools/stable/index.html
#https://neuraldatascience.io/7-eeg/erp_filtering.html


def analyse() ->int:

    run = [1, 2, 3, 4, 5, 6]
    raw_data = []
    raw_data = mne.datasets.eegbci.load_data(1, run)
    # print(raw_data)
    # for file in raw_data:
        # data = mne.io.read_raw_edf(file)
        # data_extract = data.get_data()
        # print(data_extract)
        # np.savetxt('train.csv', data_extract, delimiter = ' ')
        #Load data brut
    raw = read_raw_edf(raw_data[0], preload=True)
    #extract data
    low_cut = 0.1
    hi_cut = 30
    raw_filtered = raw.copy().filter(low_cut, hi_cut)
    raw_filtered.plot_psd()
    # events = find_events(raw)
        #Filter the data
    # event_id = {'Left': 1, 'Right': 2}
    # tmin, tmax = -1., 4.

    # picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False,
    #                exclude='bads')

    # epochs = Epochs(raw, events, event_id, tmin, tmax, proj=True, picks=picks,
    #             baseline=None, preload=True)

    # data_filtered = mne.filter(raw.get_data(), sfreq=raw.info['sfreq'], l_freq=0.5, h_freq=40)
    # print(type(data_filtered))
    print("--------")
    return 0

def main() ->int:
    
    # if len(sys.argv) != 3 :
    #     print("Wrong number of argv")
    #     return 0
    analyse()
    # data.compute_psd().plot()
    # data.plot(duration=5, n_channels=30)
    return 0

if __name__ == "__main__":
    SystemExit(main())