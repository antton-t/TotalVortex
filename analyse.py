import matplotlib.pyplot as plt
from mne.datasets import sample
from mne.io import concatenate_raws
import mne
from mne.io import read_raw_edf
from sklearn.pipeline import Pipeline


from experience import experience
from bad_channel import dropBadChannel
from data import getData

# path = "/Users/tonou/Desktop/test"
path = "/mnt/nfs/homes/antton-t/goinfre"


def analyse(subject:int, exp:int) ->int:

    runs = experience[exp]['runs']
    raw, events = getData(subject=(int(subject)), runs=runs)

    #plot raw
    raw.plot(scalings=0.0002)

    # https://www.researchgate.net/publication/326859647_A_Reproducible_MEGEEG_Group_Study_With_the_MNE_Software_Recommendations_Quality_Assessments_and_Good_Practices
    # https://www.biorxiv.org/content/biorxiv/early/2022/09/14/2022.09.12.507592.full.pdf

    spec = raw.compute_psd(fmin = 7, fmax= 30)
    spec.plot()

    # get ica
    channels = raw.info["ch_names"]
    print(len(channels))
    ica = mne.preprocessing.ICA(n_components=len(channels), random_state=0)
    ica.fit(raw)
    ica.plot_components(outlines='head', inst=raw, show_names=False)


    return 0