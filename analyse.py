import matplotlib.pyplot as plt
from mne.datasets import sample
from mne.io import concatenate_raws
import mne
from mne.io import read_raw_edf


from experience import experience
from bad_channel import dropBadChannel

# path = "/Users/tonou/Desktop/test"
path = "/mnt/nfs/homes/antton-t/goinfre"


def analyse(subject:int, exp:int) ->int:

    runs = experience[exp]['runs']
    raw_data = mne.datasets.eegbci.load_data(int(subject), runs, path=path)

    # get all the data needed in one
    raw = concatenate_raws([read_raw_edf(data, preload=True) for data in raw_data])
    mne.datasets.eegbci.standardize(raw)

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

    # filter bad channel
    # badChannelSelec = raw.info['bads']
    # print(badChannelSlec)
    #Define electrode locations
    montage = mne.channels.make_standard_montage('biosemi64') # 64 electrodes
    raw.set_montage(montage, on_missing='ignore')

    spec = raw.compute_psd(fmin = 7, fmax= 30)
    spec.plot()

    raw = dropBadChannel(raw)
    channels = raw.info["ch_names"]
    ica = mne.preprocessing.ICA(n_components=len(channels) - 2, random_state=0)
    channel_name = {'T9', 'T10'}
    raw.drop_channels(ch_names=channel_name, on_missing='ignore')
    ica.fit(raw)
    ica.plot_components(outlines='head', inst=raw, show_names=False)

    return 0