import sys
import numpy as np
import mne
from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score
from sklearn.metrics import accuracy_score
import time


from experience import experience
from data import getData
from utils import getPath
from utils import *
from colors import colors


def predict(subject:int, exp:int) ->int:

    runs = experience[exp]['runs']
    raw, events = getData(subject=(int(subject)), runs=runs)

    raw.notch_filter(60, picks='eeg', method="iir")
    raw.filter(5.0, 40.0, fir_design="firwin", skip_by_annotation="edge")

    # Read epochs
    tmin, tmax = -1.0, 4.0
    events, event_id = mne.events_from_annotations(raw, verbose=50)
    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False)
    epochs = mne.Epochs(raw, events, event_id, tmin, tmax, proj=True, picks=picks, baseline=None, preload=True, verbose=50)
    labels = epochs.events[:, -1]
    epochs_train = epochs.copy().crop(tmin=1.0, tmax=4.0).get_data()

    cv = ShuffleSplit(10, test_size=0.2, random_state=0)

    _, X_test, _, y_test = train_test_split(epochs_train, labels, train_size=0.8, random_state=0)

    save_path = SAVE_PATH + "/sub" + str(subject) + "/exp" + str(exp)
    model = joblib.load(save_path + str(exp))

    predict = model.predict(X_test)
    for i, (pred, true) in enumerate(zip(predict, y_test), start = 1) :
        print(f"Epoch {i}")
        print(f"real {true} ==> prediction {pred}")
        time.sleep(1)

    score = accuracy_score(predict, y_test)

    if (score >= 60) :
        print(f"{colors.Blue}Accuracy score => {str(score)}{colors.Reset}")
    else :
        print(f"{colors.Red}Accuracy score => {str(score)}{colors.Reset}")
    print(f"{colors.Yellow} Done ---------Subject {subject}------------- {colors.Reset}")
