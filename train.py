import pandas as pd
import mne
import sys
import numpy as np


def main() ->int:
    
    # if len(sys.argv) != 3 :
    #     print("Wrong number of argv")
    #     return 0
    raw_data = []
    np_list = []
    raw_data = mne.datasets.eegbci.load_data(4, 6)
    # print(raw_data)
    for file in raw_data:
        data = mne.io.read_raw_edf(file)
        data_extract = data.get_data()
        np.savetxt('train.csv', data_extract, delimiter = ' ')
        print("--------")
    data.compute_psd().plot()
    data.plot(duration=5, n_channels=30)
    return 0

if __name__ == "__main__":
    SystemExit(main())