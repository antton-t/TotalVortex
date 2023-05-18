from sklearn.pipeline import Pipeline
import CSP
import mne

from experience import experience
from bad_channel import dropBadChannel

path = "/mnt/nfs/homes/antton-t/goinfre"

def train(subject:int, exp:int) ->int:

    runs = experience[exp]['runs']
    raw_data = mne.datasets.eegbci.load_data(int(subject), runs, path=path)

    # get all the data needed in one
    raw = mne.io.concatenate_raws([mne.io.read_raw_edf(data, preload=True) for data in raw_data])
    mne.datasets.eegbci.standardize(raw) #set channel names

    #Define electrode locations
    montage = mne.channels.make_standard_montage('biosemi64') # 64 electrodes
    raw.set_montage(montage, on_missing='ignore')

    raw = dropBadChannel(raw)

    #Filter raw
    raw.filter(7, 30)
    event_id = {'T1': 1, 'T2': 2}  # Define the event IDs
    events, _ = mne.events_from_annotations(raw, event_id=event_id)
    # Creating annotation from events
    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude='bads')

    #Epochs
    epochs = mne.Epochs(raw, events, event_id, tmin=-1., tmax=4., proj=True, picks=picks, baseline=None, preload=True)
    epochs_train = epochs.copy().crop(tmin=1., tmax=2.)
    

    return 0