from sklearn.pipeline import Pipeline
import mne
import numpy as np
from sklearn.model_selection import ShuffleSplit, cross_val_score, train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from mne.decoding import CSP
import matplotlib.pyplot as plt
import os
import joblib

from CSP import CSP
from experience import experience
from bad_channel import dropBadChannel
from data import getData
from colors import colors

from utils import *

# https://www.youtube.com/watch?v=t-twhNqgfSY
# https://mne.tools/stable/auto_examples/decoding/decoding_csp_eeg.html

# path = "/mnt/nfs/homes/antton-t/goinfre"
path = "/mnt/nfs/homes/antton-t/goinfre"


def train(subject:int, exp:int) ->int:

    runs = experience[exp]['runs']
    raw, events = getData(subject=(int(subject)), runs=runs)

    # Apply band-pass filter
    raw.filter(7.0, 40.0, fir_design="firwin", skip_by_annotation="edge")

    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude='bads')
    
    # See epochs
    events, event_id = mne.events_from_annotations(raw)
    epochs = mne.Epochs(raw=raw,events=events, event_id=event_id, tmin = -1., tmax=4., proj=True, picks=picks, baseline=None, preload=True)
    epochs_train = epochs.copy().crop(tmin=1.0, tmax=2.0)
    labels = epochs.events[:, -1]

    # Define a monte-carlo cross-validation generator (reduce variance):
    scores = []
    epochs_data = epochs.get_data()
    epochs_data_train = epochs_train.get_data()
    
    csp = CSP(n_components=6)
    lda = LinearDiscriminantAnalysis()
    clf = Pipeline([("CSP", csp), ("LDA", lda)])

    # fit our pipeline to the experiment
    X_train, _, Y_train, _ = train_test_split(epochs_data_train, labels, random_state=0)
    clf.fit(X_train, Y_train)
    
    scores = cross_val_score(clf, epochs_data_train, labels, n_jobs=None)
    scores_mean = np.mean(scores).round(2)

    # Printing the results
    class_balance = np.mean(labels == labels[0])
    class_balance = max(class_balance, 1.0 - class_balance)
   
    # Save classifier
    save_path = SAVE_PATH + "/sub" + str(subject) + "/exp" + str(exp)

    os.makedirs(save_path, exist_ok=True)
    joblib.dump(clf, save_path + str(exp), compress=0, protocol=None, cache_size=None)

    if scores_mean >= 0.5 :
        print(f"{colors.Green}Cross ValScore {str(scores_mean)}{colors.Reset}")
    else :
        print(f"{colors.Red}Cross ValScore {str(scores_mean)} {colors.Reset}")
    print(f"{colors.Yellow}Done ---------Subject {subject}------------- {colors.Reset}")

    return 0
