from mne.io import concatenate_raws
import mne
from mne.io import read_raw_edf

from experience import experience
from bad_channel import dropBadChannel

# path = "/Users/tonou/Desktop/test"
path = "/mnt/nfs/homes/antton-t/goinfre"

def getData(subject, runs):

    raw_data = mne.datasets.eegbci.load_data(subject=subject, runs=runs, path=path)

    # get all the data needed in one
    raw = concatenate_raws([read_raw_edf(data, preload=True) for data in raw_data])
    mne.datasets.eegbci.standardize(raw)

    # Define the event IDs
    event_id = {'T1': 1, 'T2': 2}
    events, _ = mne.events_from_annotations(raw, event_id=event_id)

    # Creating annotation from events
    sfreq = raw.info["sfreq"]
    event_desc = {0: "rest", 1: "left fist", 2: "right fist"}
    annotations = mne.annotations_from_events(events=events, event_desc=event_desc, sfreq=sfreq)

    # set annotation dans le raw
    raw = raw.set_annotations(annotations=annotations)

    #Define electrode locations
    montage = mne.channels.make_standard_montage('biosemi64') # 64 electrodes
    raw.set_montage(montage, on_missing='ignore')

    # spec = raw.compute_psd(fmin = 7, fmax= 30)

    raw = dropBadChannel(raw)
    channels = raw.info["ch_names"]
    channel_name = {'T9', 'T10'}
    raw.drop_channels(ch_names=channel_name, on_missing='ignore')

    return raw, events

