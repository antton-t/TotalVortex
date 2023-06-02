import sys
import numpy as np
import mne
from sklearn.model_selection import train_test_split, ShuffleSplit, cross_val_score
from sklearn.metrics import accuracy_score


from experience import experience
from data import getData
from utils import getPath
from utils import *


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
    print("+++++++++++++++++++++++")
    print(labels)
    print("--------------------------")
    epochs_train = epochs.copy().crop(tmin=1.0, tmax=4.0).get_data()
    print(epochs_train.shape)
    print("++++++++++++++++++++++++++++")

    cv = ShuffleSplit(10, test_size=0.2, random_state=0)

    _, X_test, _, y_test = train_test_split(epochs_train, labels, train_size=0.8, random_state=0)

    save_path = SAVE_PATH + "/sub" + str(subject) + "/exp" + str(exp)
    model = joblib.load(save_path + str(exp))

    predict = model.predict(X_test)

    score = accuracy_score(predict, y_test)

    print('Accuracy score = ' + str(score))
