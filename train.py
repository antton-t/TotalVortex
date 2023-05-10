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
import tkinter as tk


#https://physionet.org/content/eegmmidb/1.0.0/
#https://scikit-learn.org/stable/index.html
#https://mne.tools/stable/index.html
#https://neuraldatascience.io/7-eeg/erp_filtering.html
path = "/Users/tonou/Desktop/test"

def analyse() ->int:

    runs = [3, 4, 7]
    raw_data = mne.datasets.eegbci.load_data(1, runs, path=path)

    # get all the data needed in one
    raw = concatenate_raws([read_raw_edf(data, preload=True) for data in raw_data])
    # mne.datasets.eegbci.standardize(raw)

    event_id = {'T1': 1, 'T2': 2}  # Define the event IDs
    events, _ = mne.events_from_annotations(raw, event_id=event_id)
    # Creating annotation from events
    sfreq = raw.info["sfreq"]
    event_desc = {0: "rest", 1: "left fist", 2: "right fist"}
    annotations = mne.annotations_from_events(events=events, event_desc=event_desc, sfreq=sfreq)
    # mne.annotations_from_events?
    # set annotation dans le raw
    raw = raw.set_annotations(annotations=annotations)
    raw.plot(scalings=0.0002)

    # #Define electrode locations
    mne.datasets.eegbci.standardize(raw=raw)
    montage = mne.channels.make_standard_montage('biosemi64') # 64 electrodes
    raw.set_montage(montage, on_missing='ignore')
    # montage.plot()

    spec = raw.compute_psd(fmin = 7, fmax= 30)
    spec.plot()

    channels = raw.info["ch_names"]
    ica = mne.preprocessing.ICA(n_components=len(channels) - 2, random_state=0)
    channel_name = {'T9', 'T10'}
    raw.drop_channels(ch_names=channel_name, on_missing='ignore')
    ica.fit(raw)
    ica.plot_components(outlines='head')

    return 0

def main() ->int:
    
    # Create a Tkinter window
    window = tk.Tk()
    window.title("TotalVortex")
    window.geometry("800x600")

    # Define the options
    options = ["Option 1", "Option 2", "Option 3"]

    # Create a variable to store the selected option
    selected_option = tk.StringVar()

    # Create the option menu widget
    option_menu = tk.OptionMenu(window, selected_option, *options)

    # Add the option menu to the main window
    option_menu.pack()

    # Create a function to print the selected option
    def print_option():
        print(selected_option.get())

    # Create a button to trigger the print function
    buttonOption = tk.Button(window, text="Print Option", command=print_option)
    
    # Create a button widget
    button = tk.Button(window, text="Train")
    button1 = tk.Button(window, text="Analyse")

    # Add the button to the main window
    button.pack()
    button1.pack()
    buttonOption.pack()


    # Start the main event loop
    window.mainloop()
    # Handle events
    # analyse()
    # data.compute_psd().plot()
    # data.plot(duration=5, n_channels=30)
    print("Bye see you soon")
    return 0

if __name__ == "__main__":
    SystemExit(main())