import pickle
import warnings
import numpy as np
from voice_gender.features import extract_features
from os.path import join, dirname

warnings.filterwarnings("ignore")


class GenderClassifier:
    females_model_path = join(dirname(__file__), "models", "females.gmm")
    males_model_path = join(dirname(__file__), "models", "males.gmm")
    # load models
    females_gmm = pickle.load(open(females_model_path, 'rb'))
    males_gmm = pickle.load(open(males_model_path, 'rb'))

    @staticmethod
    def score(audio):
        if isinstance(audio, str):  # file path
            audio = extract_features(audio)

        is_female = np.array(GenderClassifier.females_gmm.score(audio)).sum()
        is_male = np.array(GenderClassifier.males_gmm.score(audio)).sum()
        return {"male": is_male, "female": is_female}

    @staticmethod
    def predict(audio):
        if isinstance(audio, str):  # file path
            audio = extract_features(audio)

        is_female = np.array(GenderClassifier.females_gmm.score(audio)).sum()
        is_male = np.array(GenderClassifier.males_gmm.score(audio)).sum()
        if is_male > is_female:
            return "male"
        else:
            return "female"


if __name__ == "__main__":
    print(GenderClassifier.predict("examples/utterance_2019-04-24T20:54:52.460914.wav"))
    print(GenderClassifier.score("examples/utterance_2019-04-24T20:54:52.460914.wav"))
