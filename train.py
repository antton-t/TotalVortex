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
from tkinter import ttk


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

def selectAll():
    print("Test")

def main() ->int:
    
    # Create a Tkinter window
    window = tk.Tk()
    window.title("TotalVortex")
    window.geometry("800x600")

    # Define the option for Subject
    subjectFont = tk.LabelFrame(window, text="Subject")
    subjectFont.pack(padx=10, pady=10)
    subjectVar = tk.StringVar()
    subjectVar.set("Select the Subject")
    options = ["All", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5", "Subject 6", "Subject 7", "Subject 8", "Subject 9", "Subject 10", "Subject 11", "Subject 12", "Subject 13", "Subject 14", "Subject 15", "Subject 16", "Subject 17", "Subject 18", "Subject 19", "Subject 20", "Subject 21", "Subject 22", "Subject 23", "Subject 24", "Subject 25", "Subject 26", "Subject 27", "Subject 28", "Subject 29", "Subject 30", "Subject 31", "Subject 32", "Subject 33", "Subject 34", "Subject 35", "Subject 36", "Subject 37", "Subject 38", "Subject 39", "Subject 40", "Subject 41", "Subject 42", "Subject 43", "Subject 44", "Subject 45", "Subject 46", "Subject 47", "Subject 48", "Subject 49", "Subject 50", "Subject 51", "Subject 52", "Subject 53", "Subject 54", "Subject 55", "Subject 56", "Subject 57", "Subject 58", "Subject 59", "Subject 60", "Subject 61", "Subject 62", "Subject 63", "Subject 64", "Subject 65", "Subject 66", "Subject 67", "Subject 68", "Subject 69", "Subject 70", "Subject 71", "Subject 72", "Subject 73", "Subject 74", "Subject 75", "Subject 76", "Subject 77", "Subject 78", "Subject 79", "Subject 80", "Subject 81", "Subject 82", "Subject 83", "Subject 84", "Subject 85", "Subject 86", "Subject 87", "Subject 88", "Subject 89", "Subject 90", "Subject 91", "Subject 92", "Subject 93", "Subject 94", "Subject 95", "Subject 96", "Subject 97", "Subject 98", "Subject 99", "Subject 100", "Subject 101", "Subject 102", "Subject 103", "Subject 104", "Subject 105", "Subject 106", "Subject 107", "Subject 108", "Subject 109"]
    subjectSelect = ttk.Combobox(subjectFont, textvariable=subjectVar, values=options, state="readonly")

    # buttonAllUsers = tk.Checkbutton(window, text="Select All Users", font=("Arial", 12), command=selectAll)

    button1 = tk.Checkbutton(window, text="Open and close left or right fist", font=("Arial", 12))
    button2 = tk.Checkbutton(window, text="Imagine opening and closing Left or right fist", font=("Arial", 12))
    button3 = tk.Checkbutton(window, text="Open and close both fists or both feet", font=("Arial", 12))
    button4 = tk.Checkbutton(window, text="Imagine opening and closing both fists or both feet", font=("Arial", 12))

    # Create a button widget
    buttonTrain = tk.Button(window, text="Train")
    buttonAnalyse = tk.Button(window, text="Analyse")
    
    # Add the button to the main window
    subjectSelect.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    buttonTrain.pack()
    buttonAnalyse.pack()

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