import joblib
import mne


SAVE_PATH = "./save"

def getPath(sub) :

    path = joblib.load(sub)
    return path