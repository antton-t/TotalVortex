import joblib
import mne


SAVE_PATH = "./save"

def getPath(sub) :

    try :
        return joblib.load(sub)
    except NameError:
        print("Need to train it first")


