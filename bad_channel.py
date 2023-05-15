import	mne

def	dropBadChannel(raw):

    channels = raw.info["ch_names"]
    # channel = ['Nz', 'F9', 'F10', 'FT9', 'FT10', 'A1', 'A2', 'TP9', 'TP10', 'P9', 'P10']
    good_channels = ["FC5", "FC3", "FC1", "FCz", "FC2", "FC4", "FC6", "C5",  "C3",  "C1",  "Cz",  "C2",  "C4",  "C6", "CP5", "CP3", "CP1", "CPz", "CP2", "CP4", "CP6"]
    out = [x for x in channels if x not in good_channels]
    raw.drop_channels(ch_names=out, on_missing='ignore')
    print(len(raw.info['ch_names']))
    return raw
