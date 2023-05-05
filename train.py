import pandas as pd
import mne
import sys
import numpy as np
from mne import Epochs, pick_types, find_events
from sklearn.pipeline import Pipeline
from mne.io import read_raw_edf
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
from mne.datasets import sample
from mne.io import concatenate_raws

#https://physionet.org/content/eegmmidb/1.0.0/
#https://scikit-learn.org/stable/index.html
#https://mne.tools/stable/index.html
#https://neuraldatascience.io/7-eeg/erp_filtering.html
path = "/mnt/nfs/homes/antton-t/goinfre"

def analyse() ->int:

    runs = [1, 2, 3]
    raw_data = mne.datasets.eegbci.load_data(1, runs, path=path)

    # get all the data needed in one
    raw = concatenate_raws([read_raw_edf(data, preload=True) for data in raw_data])
    # mne.datasets.eegbci.standardize(raw)

    # Filtering the data according to .....
    raw_filter = raw.copy().filter(7, 30)
    raw_filter.plot(scalings=0.0002)
    plt.show()

    # #Define electrode locations
    # montage = mne.channels.make_standard_montage('standard_1005')

    # #Set the electrode locations in the EEG data
    # raw.set_montage(montage)

    # # Plot the EEG data
    # raw.plot_sensors()
    # print(raw.info.ch_names)

    # Separating mixed signal
    # ica = mne.preprocessing.ICA(n_components=30, random_state=42)
    # ica.fit(raw.copy().filter(1, 30))
    # ica.plot_components()
    # plt.show()

    return 0

def main() ->int:
    
    if len(sys.argv) == 2 and (sys.argv[1]=="-h" or sys.argv[1]=="--help"):
        print("How to use it?")
        print("1st arg: 1st subjet")
        print("2nd arg: last subjet")
        exit()
    # if len(sys.argv) != 3 :
    #     print("Wrong number of argv")
    #     return 0
    else :
        analyse()
    # data.compute_psd().plot()
    # data.plot(duration=5, n_channels=30)
    return 0

if __name__ == "__main__":
    SystemExit(main())