import joblib
import mne
import json
import os

SAVE_PATH = "./save"

def getPath(sub) :

    try :
        return joblib.load(sub)
    except NameError:
        print("Need to train it first")

def getJsonValue(key, file_path = "path.json") -> str:
    if os.path.exists("path.json"):
        with open(file_path, 'r') as file:
            print("---------------")
            data = json.load(file)
    return data.get(key)
